
import pandas as pd
import numpy as np
import nltk
from nltk import ngrams
from nltk.corpus import stopwords
import string
import nltk
from langdetect import detect
import indicoio
#nltk.download('averaged_perceptron_tagger')
#nltk.download('brown')
import numpy
import numpy as np
import pandas as pd
import re, operator
from os import path
from PIL import Image
from textblob import TextBlob
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from textblob import TextBlob
import googletrans
from googletrans import Translator

# nltk.download('stopwords')
data = pd.read_csv('trafico.csv', encoding='latin-1')
print(data.head)
translator = Translator()
data_trans = translator.translate('"#traficogt la Roosevelt esta de la gran puta. Choques hacia mixco. Choques hacia tikal futura.MATENME POR LA GRAN PUTAAAA ARZU LA PUTA QUE TE PARIO. AMILCAR MONTEJO TU MADRE"')
print(data_trans.text)

blob = TextBlob(data_trans.text)
print(blob)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]
print(blob.tags)
blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])

print(blob.noun_phrases)
for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
