import requests
import json
import random



def random_qoute()-> str:
    '''gets a random qoute'''
    random_num = random.randint(0,30)
    res = requests.get('https://type.fit/api/quotes')
    res = json.loads(res.text)
    return res[random_num]['text'] 


