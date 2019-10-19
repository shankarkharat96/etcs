from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'trial.html')
def SELECT(request):
    return render(request, 'SELECT.html')
def MAP(request):
		return render(request, 'MAP.html') 
