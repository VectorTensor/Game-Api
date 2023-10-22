from sklearn import datasets
import numpy as np 

from sklearn.linear_model import LogisticRegression

from joblib import dump, load
import os


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

        x = self.loaded_model.predict(np.expand_dims(data,0))

        return self.labelDict[x]




        
