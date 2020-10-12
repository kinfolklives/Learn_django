from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render # add

# Create your views here.
def hello(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return render(request, 'home.html')

def responsewithhtml(request):
    data = {'first':'Eugene', 'second':'Choi'} # add
    return rendedr(request, 'hello/responsewithhtml.html', context=data)
