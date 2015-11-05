__author__ = 'grobvincent'

import codecs

from pymongo import MongoClient

import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS


client = MongoClient('localhost', 27017)
db = client.Medias

links = db.articles

cursor = links.find({},{"body":1})


test=""

for document in cursor :
    test=test+document['body']

with codecs.open("text_mining/my_stopwords.txt","r",encoding="utf-8") as f:
     read_data = f.readlines()

print(read_data)




stopwords = STOPWORDS.copy()
print(len(stopwords))

for data in read_data:

    stopwords.add(data)


stopwords = map(lambda s: s.strip(), stopwords)


wordcloud = WordCloud(max_words=10000, stopwords=stopwords,
               random_state=1).generate(test)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()

