from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def calculate():
    return 1

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name':"Haris"})