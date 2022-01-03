from django.urls import path, include
from .views import *
from rest_framework import routers


urlpatterns = [
    path("", snippet_list),
    path('<int:pk>/', snippet_detail),
]