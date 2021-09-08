import requests
import json

def random_qoute()-> str:
    '''gets a random qoute'''
    res = requests.get('https://type.fit/api/quotes')
    res = json.loads(res.text)
    print(res[0]['text']) 

random_qoute()
