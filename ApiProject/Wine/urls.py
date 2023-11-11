from django.urls import path 
from Wine import views


urlpatterns = [
        path('', views.WineViews.as_view()),
        ]
