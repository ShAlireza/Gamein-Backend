from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('Welcome to Homepage...')


def staffs(request):
    return HttpResponse('This is Staffs page.')