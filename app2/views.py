from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse("<h1>this is app2 in  first view</h1>")
def second(request):
    return HttpResponse("<h1>this is app2 in second view<h1>")