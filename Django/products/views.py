from django.http import HttpResponse
from django.shortcuts import render

#  /products -> index


def index(request):
    return HttpResponse("Hello World")


def new(request):
    return HttpResponse("New Products")


def byme(request):
    return HttpResponse('By Gopal')


def gdev(request):
    return HttpResponse('Created by G Developer')