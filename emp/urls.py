from django.contrib import admin
from django.urls import path,include
from .views import *
# from models import Emp

urlpatterns = [
    path ("home/",emp_home),
    path ("add-emp/",add_emp),
]
