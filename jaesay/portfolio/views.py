from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sexyDashboard(request):
    return render(request, 'sexyDashboard.html')

def cat(request):
    return render(request, 'cat.html')

def cane(request):
    return render(request, 'cane.html')

def weather(request):
    return render(request, 'weather.html')

def maze(request):
    return render(request, 'maze.html')