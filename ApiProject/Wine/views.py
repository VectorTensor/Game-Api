from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np 
from collections import deque
from .wineModel import WineModel


# Create your views here.

class WineViews(APIView):

    def get(self, request):
        return Response({"message":"send post request "})
    
    # keys : proline ,flavanoids, od280/od315_of_diluted_wines, alcohol
    def post(self, request):
        x = []
        x.append(request.data['proline'])
        x.append(request.data['flavanoids'])
        x.append(request.data['od280/od315_of_diluted_wines'])
        x.append(request.data['alcohol'])

        data = np.array(x)

        wine = WineModel()

        label = wine.wineType(data)

        return Response({"label":label})
        

