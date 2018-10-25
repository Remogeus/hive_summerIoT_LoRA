from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base.html')


def show_data(request):
    return render(request, 'show_data/index.html')
