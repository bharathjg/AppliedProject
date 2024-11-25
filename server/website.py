from flask import render_template, send_file, redirect, jsonify
from time import time
from os import urandom
from server.prompts import biographies, exercise2_prompts, exercise3_topics

path = r'C:/Users/govin/Documents/AppliedProject/Frontend/website/src/Components/chatwindow.html'
class Website:
    def __init__(self, app):
        self.app = app
        self.routes = {
            '/':{
                'function': self._index,
                'methods': ['GET', 'POST']
            },
            '/about':{
                'function': self._about,
                'methods': ['GET']
            },
            '/exercises':{
                'function': self._chat,
                'methods': ['GET', 'POST']
            },
            '/exercise1': {
                'function': self._ex1,
                'methods': ['GET', 'POST']
            },
            '/exercise2': {
                'function': self._ex2,
                'methods': ['GET', 'POST']
            },
            '/exercise3': {
                'function': self._ex3,
                'methods': ['GET', 'POST']
            },
            '/api/suggestions_ex1':{
                'function': self._suggestions_ex1,
                'methods': ['GET']
            },
            '/api/suggestions_ex2':{
                'function': self._suggestions_ex2,
                'methods': ['GET']
            },
            '/api/suggestions_ex3':{
                'function': self._suggestions_ex3,
                'methods': ['GET']
            }
        }
    
    def _index(self):
        return render_template('landing.html')
    
    def _about(self):
        return render_template('about.html')
    
    def _chat(self):
        return redirect('/exercise1')
    
    def _ex1(self):
        return render_template('ex1.html')
    
    def _ex2(self):
        return render_template('ex2.html')
    
    def _ex3(self):
        return render_template('ex3.html')
    
    def _suggestions_ex1(self):
        return jsonify(list(biographies.keys()))
    
    def _suggestions_ex2(self):
        return jsonify(list(exercise2_prompts.keys()))
    
    def _suggestions_ex3(self):
        return jsonify(exercise3_topics)

