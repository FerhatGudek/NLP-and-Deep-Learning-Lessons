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

yorum = re.sub("[^a-zA-Z]"," ",yorumlar["Review"][0]) # a dan z dışındakileri boşluk karakter ile değiştir (sıfırıncı satır için yaptı)
               
