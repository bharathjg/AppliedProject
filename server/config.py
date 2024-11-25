import os
import json

class Config:
    def __init__(self):
        with open('config.json', 'r') as f:
            data = json.load(f)
        self.openai_key = data['openai_key']
        self.openai_api_base = data['openai_api_base']
        self.site_config = data['site_config']
        self.proxy = data['proxy']