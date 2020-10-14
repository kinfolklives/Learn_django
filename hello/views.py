from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render # add
from datas import workscrapping

# Create your views here.
def hello(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return render(request, 'home.html')

def responsewithhtml(request):
    data = {'first':'Eugene', 'second':'Choi'} # add
    return render(request, 'hello/responsewithhtml.html', context=data)

def form(request):
    return render(request, 'hello/requestform.html')

def responsewithhtml02(request):
    data = dict()
    data["first"] = request.GET['first'];
    data["second"] = request.GET['second']
    return render(request, 'hello/responsewithhtml02.html', context=data)

def template(request):
    return render (request, 'hello/template.html')

