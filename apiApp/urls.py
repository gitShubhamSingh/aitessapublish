from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.Index.as_view(), name="Index"),
]
