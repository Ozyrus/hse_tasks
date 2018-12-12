from string import punctuation
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer
import re
from nltk import bigrams
from nltk import trigrams
from nltk import ngrams
morph = MorphAnalyzer()
punct = punctuation+'«»—…“”*№–' 
stops = stopwords.words('russian')
from nltk.tokenize import word_tokenize
#вот так можно расширить стоп-слова
stops.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'к', 'на', 'хоть', 'после'])
def normalize(text):   
    words = [word.strip(punct) for word in word_tokenize(text.lower())]
    words = [morph.parse(word)[0].normal_form for word in words]
    words = [word for word in words if word not in stops]
    return ' '.join(words)


#n = 6
#sixgrams = ngrams(text.split(), n)

#for grams in sixgrams:
#  print grams

with open('texts.txt', 'r') as openfile:
  contents = openfile.read()
  print(normalize(contents))
