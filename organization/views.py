from django.shortcuts import render

# Create your views here.
def name(request):
    return render(request, 'organization/name.html')
    
def tel():
    return render(request, 'organization/tel.html')

def address():
    return render(request, 'organization/address.html')