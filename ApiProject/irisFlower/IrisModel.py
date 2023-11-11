from sklearn import datasets
import numpy as np 

from sklearn.linear_model import LogisticRegression

from joblib import dump, load
import os
from sklearn.preprocessing import StandardScaler

class IrisModel:
    def __init__(self) -> None:
        pth = os.path.dirname(__file__)
        self.loaded_model = load(os.path.join(pth,'iris.joblib'))
        self.labelDict = {
                0:  'setosa',
                1: 'versicolor',
                2: 'virginica'
                }


    def flowerType(self, data):
        sc = StandardScaler()
        x = sc.fit_transform(np.expand_dims(data,0))
        x = self.loaded_model.predict(x)

        return self.labelDict[x[0]]




        
