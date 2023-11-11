from django.urls import path 
from Wine import views


urlpatterns = [
        path('', views.IrisView.as_view()),
        ]
