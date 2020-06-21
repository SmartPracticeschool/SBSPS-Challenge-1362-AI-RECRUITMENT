from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate. login, logout
from djang.contrib.auth.models import User
def index(request):
    return HttpResponse('<em>In Candidate Arena</em>')


def login(request):
    pass


def logout(request):
    pass