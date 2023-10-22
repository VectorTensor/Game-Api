from django.urls import path 
from irisFlower import views


urlpatterns = [
        path('', views.IrisView.as_view()),
        ]
