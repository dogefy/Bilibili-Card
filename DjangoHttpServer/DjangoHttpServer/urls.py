from django.urls import path
from . import views

urlpatterns = [
    path('card/', views.card),
]
