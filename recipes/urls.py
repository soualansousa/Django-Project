from django.contrib import admin
from django.urls import path
from recipes.views import contato, home


urlpatterns = [
    path('', home),
    path('contato/', contato),
]