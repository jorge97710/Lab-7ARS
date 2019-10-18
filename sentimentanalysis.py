
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


# nltk.download('stopwords')
data = pd.read_csv('trafico.csv', encoding='latin-1')
print(data.head)
indicoio.config.api_key = 'YOUR_API_KEY';
print("Top words")
indicoio.sentiment = "El agua ya afecta La Fontana zona 4. Urgen acciones @netobran, @MuniMixco_. También la conexión a Bosques.prensa_libre @EmisorasUnidas @Guatevision_tv @CanalAntigua @TN23NOTICIAS @info502 @traficogt @soy_502 #traficogt @vinicionoti7 @NuevoMundoGT @Noti7Guatemala @TelediarioGT https://t.co/QfEe0vcjmJ"
print (indicoio.sentiment)

