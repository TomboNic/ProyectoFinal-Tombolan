from functools import reduce
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html", {})