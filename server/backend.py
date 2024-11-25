from json import dumps
from time import time
from flask import request, jsonify, Response
from hashlib import sha256
from datetime import datetime
import requests 
import json
import os
from server.prompts import biographies, context_ex1, context_ex2, context_ex3

from server.utils import separate_text_string


class Backend_Api:
    def __init__(self, app, config) -> None:
        self.app = app
        self.openai_key = config.openai_key
        self.openai_api_base = config.openai_api_base
        self.proxy = config.proxy
        self.routes = {
            '/send_message': {
                'function': self.send_message_stream,
                'methods': ['POST']
            }
        }
    
    def _exercise1(self):
        return
    
    def _exercise2(self):
        return
    
    def _exercise3(self):
        return
    
    def send_message(self):

        system_prompt = context_ex1
        user_prompt = request.get_json().get('user_prompt')
        user_choice = user_prompt.split()[-2:]
        user_choice = ' '.join(user_choice)
        print(user_choice)
        user_prompt_suffix = f"This is the biography to edit: {biographies[user_choice]}"
        
        url = "https://api.openai.com/v1/chat/completions"

        payload = json.dumps({
        "model": "gpt-4o",
        "messages": [
            {
            "role": "system",
            "content": system_prompt
            },
            {
            "role": "user",
            "content": user_prompt+" "+user_prompt_suffix,
            }
        ]
        
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {self.openai_key}',
        'Cookie': '__cf_bm=5xUoed.SbZJiVGV.OArs7Tc07MBD6SbiTV5eyfeh8WE-1729718278-1.0.1.1-om.EwXECFWySkxducOqWsJWVIBbksb0dMCpsfjtdmIHER2mzAESiQhGsZqfOaJCJ3JNe9Q2EglsK1AcvOwPzdQ; _cfuvid=CVk4srq60lLYhDm.uQET_dEi99hwA.jQ0ne.mba5ePk-1729718278014-0.0.1.1-604800000'
        }

        srv_response = requests.post(url, headers=headers, data=payload)
        data = srv_response.text
        jsondata = json.loads(data)
        response = jsondata['choices'][0]['message']['content']
        text, errors = separate_text_string(response)
        #return self.app.response_class(self.stream(srv_response), mimetype='text/event-stream')
        print(errors)
        return jsonify({'response':text, 'errors':errors})
    

    def send_message_stream(self):
        system_prompt = ""
        user_prompt = request.get_json().get('user_prompt')
        exercise = int(request.get_json().get('exercise'))

        if exercise == 1:
            system_prompt = context_ex1
            user_choice = ' '.join(user_prompt.split()[-2:])
            print(user_choice)
            user_prompt_suffix = f"This is the biography to edit: {biographies[user_choice]}"
            user_prompt = user_prompt + ". " + user_prompt_suffix
        
        elif exercise == 2:
            system_prompt = context_ex2
        
        elif exercise == 3:
            system_prompt = context_ex3
            user_choice = ' '.join(user_prompt.split()[-2:])
            print(user_choice)
            user_prompt = user_prompt + " Keep it brief."
        
        url = "https://api.openai.com/v1/chat/completions"

        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            "stream": True
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.openai_key}'
        }

        def generate():
            try:
                with requests.post(url, headers=headers, json=payload, stream=True) as response:
                    response.raise_for_status()
                    for line in response.iter_lines():
                        if line:
                            line = line.decode('utf-8')
                            if line.startswith('data: '):
                                data = line[6:]
                                if data == '[DONE]':
                                    break
                                try:
                                    chunk = json.loads(data)
                                    content = chunk['choices'][0]['delta'].get('content', '')
                                    if content:
                                        yield f"data: {content}\n\n"
                                except json.JSONDecodeError:
                                    print(f"Error decoding JSON: {data}")
            except requests.RequestException as e:
                print(f"Error making request: {e}")
                yield f"data: Error: {str(e)}\n\n"

        return Response(generate(), mimetype='text/event-stream')