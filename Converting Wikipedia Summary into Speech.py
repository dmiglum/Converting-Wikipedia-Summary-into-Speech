# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:38:08 2022

@author: Dmitriy Glumov
"""


import gensim
import re
from gensim.summarization.summarizer import summarize #old version 3.8.3
import requests
from bs4 import BeautifulSoup
import pyttsx3


url = 'https://en.wikipedia.org/wiki/Machine_learning'

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')

articles = []
for i in range(len(soup.select('p'))):
    article = soup.select('p')[i].getText().strip()
    articles.append(article)
articlecontent = " ".join(articles)

summary = summarize(articlecontent, ratio = 0.01)
summary = re.sub('\[[^\]]*\]','',summary) 
print(summary)

#converting text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 130                       ## Reduce The Speech Rate
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
  
speak(summary)
# engine.save_to_file(summary, 'test.mp3') #saving speech as an audio file
engine.runAndWait()

