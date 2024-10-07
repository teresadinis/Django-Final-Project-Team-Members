from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('<h1>Viva D040!</h1>')

def welcome(request):
    return render(request, 'app1/welcome.html',{'nome':'Teresa'})