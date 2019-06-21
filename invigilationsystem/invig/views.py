from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'invig/login.html')



def profile(request):
    return render(request, 'invig/profile.html')