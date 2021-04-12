import json
import datetime
import os
from urllib import request
import wordnik

# def wordOfDay():
now=datetime.datetime.now()
today=str(now.year)+'-'+str(now.month)+'-'+str(now.day)
url='http://api.wordnik.com:80/v4/words.json/wordOfTheDay?date='+today+'&api_key=d52b63b6880f17811310d0fbd3b0d3a8ef163a248f58dc831'
response=request.urlopen(url)
data=response.read()
jsonData=json.loads(data)
for word in jsonData:
    w=word["word"]
    m=word['definitions'][0]['text']
    n=word['note']
# print(jsonData)
# print(jsonData["word"])
# print(jsonData["definitions"][0]['text'])
# print(jsonData["note"])
# x=word['word']
# wordOfDay()