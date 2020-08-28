from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(response):
    return HttpResponse("<h1>test</h1>")


def login(response):
    return HttpResponse("<h1>login page</h1>")
