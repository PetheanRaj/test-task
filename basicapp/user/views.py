from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def userid(request):
    return HttpResponse("User ID File")