from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<em>In Recruiters Arena</em>')
