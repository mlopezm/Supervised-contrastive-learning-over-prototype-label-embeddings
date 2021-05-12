# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 00:34:13 2016

@author: Manuel
"""


from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import pandas.core.algorithms as algos
from pandas import Series
import numpy as np


def one_hot_dataframe(data, cols, replace=False):
    vec = DictVectorizer()
    mkdict = lambda row: dict((col, row[col]) for col in cols)
    vecData = pd.DataFrame(vec.fit_transform(data[cols].apply(mkdict, axis=1)).toarray())
    vecData.columns = vec.get_feature_names()
    vecData.index = data.index
    if replace is True:
        data = data.drop(cols, axis=1)
        data = data.join(vecData)
    return (data, vecData, vec)

