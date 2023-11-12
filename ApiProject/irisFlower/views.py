from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np
from collections import deque
from .IrisModel import IrisModel

class IrisView(APIView):
    
    def get(self, request):

        return Response({"message":"send post request with petal size. keys: height ,width"})

    def post(self, request):
        x = float(request.data['height'])
        y = float(request.data['width'])
        data = np.array([x,y])
        irisModel = IrisModel()
        label = irisModel.flowerType(data) 

        return Response({"label":label})

        

