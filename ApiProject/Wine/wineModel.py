from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
from joblib import load
import os
from sklearn.preprocessing import StandardScaler
class WineModel:
    def __init__(self):
        pth = os.path.dirname(__file__)
        self.loaded_model = load(os.path.join(pth, 'wine.joblib'))
        self.labelDict = {
            0 : 'class 1',
            1 : 'class 2',
            2 : 'class 3'
        }

    def wineType(self, data):
        sc = StandardScaler()
        x = sc.fit_transform(np.expand_dims(data,0))
        x = self.loaded_model.predict(x)
        return self.labelDict[x[0]]
    
