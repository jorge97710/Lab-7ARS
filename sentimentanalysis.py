
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
import seaborn as sea
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
sea.countplot(data['Tweet Type'])
plt.show()
sea.countplot(data['Media Type'])
plt.show()
sea.countplot(data['Name'])
plt.show()
sea.countplot(data['Screen Name'])
plt.show()
sea.countplot(data['Created At'])
plt.show()
sea.countplot(data['Language'])
plt.show()
datos = data.tail(500)
print(datos)
mystring = str(datos)
print("DATOS",mystring)
print("--------------------------------------------------------------------------")
result = mystring.split()
print (result)

print ("The total number of words is: "  + str(len(result)))
print ("The word 'bran' occurs: " + str(result.count("bran")))

translator = Translator()
#en base a los top 10 mentions se obtuvo el siguiente 
data_trans = translator.translate('""El agua ya afecta La Fontana zona 4. Urgen acciones @netobran, @MuniMixco_. También la conexión a Bosques.@prensa_libre @EmisorasUnidas @Guatevision_tv @CanalAntigua @TN23NOTICIAS @info502 @traficogt @soy_502 #traficogt @vinicionoti7 @NuevoMundoGT @Noti7Guatemala @TelediarioGT https://t.co/QfEe0vcjmJ""')
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
    print ("---------------------1--------------------------")
    print(sentence.sentiment.polarity)

data_trans = translator.translate('""#traficogt la Roosevelt esta de la gran puta. Choques hacia mixco. Choques hacia tikal futura.MATENME POR LA GRAN PUTAAAA ARZU LA PUTA QUE TE PARIO. AMILCAR MONTEJO TU MADRE""')
blob = TextBlob(data_trans.text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])
for sentence in blob.sentences:
    print ("---------------------2--------------------------")
    print(sentence.sentiment.polarity)

data_trans = translator.translate('Gracias @netobran @MuniMixco_ @EmixtraPablo @EmixtraGT @PMTdeMixco hoy si se lucieron con los policías del A-10, hicieron el peor tráfico del año, no saben controlar sus tiempos, los invito a que vean cámaras #TraficoGT #traficomixco')
blob = TextBlob(data_trans.text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])
for sentence in blob.sentences:
    print ("---------------------3--------------------------")
    print(sentence.sentiment.polarity)
data_trans = translator.translate('Don Neto prende ayudar a los vecinos d Mixco perjudicando al Occidente de Guatemala tapando un carril  completo de la ruta Interamericana @netobran @LordTortrix #traficogt #transitogt @DrGiammattei @amilcarmontejo #guatemalapower https://t.co/nEwecoMgxm')
blob = TextBlob(data_trans.text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])
for sentence in blob.sentences:
    print ("---------------------4--------------------------")
    print(sentence.sentiment.polarity)
data_trans = translator.translate('"""Hay no me di cuenta que iba la placa tapada... los patojos deben de haberlo hecho!""#TraficoGT #traficovn @SantosDalia @amilcarmontejo @PMT_VILLANUEVA https://t.co/IX72i7tE5l"')
blob = TextBlob(data_trans.text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])
for sentence in blob.sentences:
    print ("---------------------5--------------------------")
    print(sentence.sentiment.polarity)

data_trans = translator.translate('"Una hora para recorrer 1.2 km shit, qué deberían pasarse en 11 minutos.  De campo real al semáforo de granjas para salir al Boulevard Villa deportiva. #TraficoGT @EmixtraPablo @EmixtraGT @PMTdeMixco https://t.co/9JK9Z26Xlm"')
blob = TextBlob(data_trans.text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])
for sentence in blob.sentences:
    print ("---------------------6--------------------------")
    print(sentence.sentiment.polarity)

data_trans = translator.translate('Todos los días en la 12 Av a inmediaciones del Digecam en la zona 5 = CAOS #EmetraNoSirve @amilcarmontejo @muniguate #TraficoGT @AlcaldeQuinonez https://t.co/TzCGKy1GcX')
blob = TextBlob(data_trans.text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])
for sentence in blob.sentences:
    print ("---------------------7--------------------------")
    print(sentence.sentiment.polarity)

data_trans = translator.translate('"Ya evaluaron que hacer con el gran mierda que se hace en la U para el carmen ???? Cada día es peor. #TraficoGT @amilcarmontejo @SantosDalia @netobran"')
blob = TextBlob(data_trans.text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])
for sentence in blob.sentences:
    print ("---------------------8--------------------------")
    print(sentence.sentiment.polarity)

data_trans = translator.translate('#TraficoGT lento sobre la 14 calle y Avenida Reforma por actividad en hotel del sector. Utilice vías alternas vía @1000tonsandoval @amilcarmontejo @muniguate https://t.co/VEwuh1ZAkA')
blob = TextBlob(data_trans.text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])
for sentence in blob.sentences:
    print ("---------------------9--------------------------")
    print(sentence.sentiment.polarity)

data_trans = translator.translate('#TraficoGT lento sobre la 14 calle y Avenida Reforma por actividad en hotel del sector. Utilice vías alternas vía @1000tonsandoval @amilcarmontejo @muniguate https://t.co/VEwuh1ZAkA')
blob = TextBlob(data_trans.text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),

                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',

                    #            'ultimate movie monster',

                    #            'amoeba-like mass', ...])
for sentence in blob.sentences:
    print ("---------------------9--------------------------")
    print(sentence.sentiment.polarity)
