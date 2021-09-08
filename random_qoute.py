import requests
import json
import random

random_num = random.randint(1,30)

def random_qoute()-> str:
    '''gets a random qoute'''
    res = requests.get('https://type.fit/api/quotes')
    res = json.loads(res.text)
    return res[random_num]['text'] 


