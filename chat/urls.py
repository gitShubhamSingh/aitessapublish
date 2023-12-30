from django.urls import path
from . import views

urlpatterns =[
    path('createIndex/', views.IndexChat.as_view(), name="IndexChat"),
    path('askChat/', views.AskChat.as_view(), name="AskChat")
]