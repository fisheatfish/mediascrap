__author__ = 'grobvincent'

import codecs

from os import path
import Image
import numpy as np
import matplotlib.pyplot as plt
import random
from pymongo import MongoClient

import matplotlib.pyplot as plt

import Image

from wordcloud import WordCloud, STOPWORDS

from scipy.misc import imread



client = MongoClient('localhost', 27017)
db = client.Medias

links = db.articles

cursor = links.find({},{"body":1})


test=""

for document in cursor :
    test=test+document['body']

with codecs.open("text_mining/my_stopwords.txt","r",encoding="utf-8") as f:
     read_data = f.readlines()





stopwords = STOPWORDS.copy()


for data in read_data:

    stopwords.add(data)


stopwords = map(lambda s: s.strip(), stopwords)


mask_choko = np.array(Image.open("text_mining/chokomag.png"))


wordcloud = WordCloud( stopwords=stopwords,background_color="black", max_words=10000,mask=mask_choko).generate(test)



plt.title("Chokomag")
plt.imshow(wordcloud)
wordcloud.to_file("text_mining/chokomag_wc.png")
plt.axis("off")
plt.figure()
plt.imshow(mask_choko, cmap=plt.cm.gray)
plt.axis("off")
plt.show()