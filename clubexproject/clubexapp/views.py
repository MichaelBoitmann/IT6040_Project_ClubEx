from django.shortcuts import HttpResponse, render

def index(request):
    return HttpResponse("Hello, world. Yay it works.")
