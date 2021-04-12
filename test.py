import json
import datetime
import os
from urllib import request
import wordnik

def wordOfDay():
    now=datetime.datetime.now()
    today=str(now.year)+'-'+str(now.month)+'-'+str(now.day)
    url='http://api.wordnik.com:80/v4/words.json/wordOfTheDay?date='+today+'&api_key=d52b63b6880f17811310d0fbd3b0d3a8ef163a248f58dc831'
    response=request.urlopen(url)
    data=response.read()
    jsonData=json.loads(data)
    # print(jsonData)
    for word in jsonData:
        w=jsonData["word"]
        m=jsonData['definitions'][0]['text']
        n=jsonData["note"]
    res=f"Word: {w}""\n"f"Meaning: {m}""\n"f"Note: {n}"
    return res
# print(w)
# print(m)
# print(n)


# print(jsonData)
# print(jsonData["word"])
# print(jsonData["definitions"][0]['text'])
# print(jsonData["note"])
# x=word['word']
print(wordOfDay())