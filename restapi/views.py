from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(reqest):
    return HttpResponse("하나를 배우면 열을 잊는다 ㅠㅠ")
