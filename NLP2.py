# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 23:50:07 2025

@author: ferha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

yorumlar = pd.read_csv("restaurant_comments.csv")
print(yorumlar)

yorum = re.sub("[^a-zA-Z]"," ",yorumlar["Review"][3]) # a dan z dışındakileri boşluk karakter ile değiştir (sıfırıncı satır için yaptı)
               
yorum = yorum.lower() # 3. işareti metin dizisi küçük harflere döndü
yorum = yorum.upper() # 3. işaretli metin dizisi büyük harflere dönüştü
yorum = yorum.split() # 3. işaretli metin dizisi bölünür (kelime kelime)
print(yorum)

import nltk
nltk.download("stopwords")
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


nltk.download("stopwords")
from nltk.corpus import stopwords

derlem = []

for i in range(1000):
    yorum = re.sub("[^a-zA-Z]"," ",yorumlar["Review"][i])
    yorum = yorum.lower()
    yorum = yorum.split()
    yorum = [ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words("english"))]
    yorum = " ".join(yorum)
    derlem.append(yorum)