from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to Top Athletes Home Page')

def baseball(request):
    return render(request, 'baseball.html')

def basketball(request):
    return HttpResponse('<h1>Welcome to Top Athletes Basketball Page')

def football(request):
    return HttpResponse('<h1>Welcome to Top Athletes Football Page')

def hockey(request):
    return HttpResponse('<h1>Welcome to Top Athletes Hockey Page')

