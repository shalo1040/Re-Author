from django.shortcuts import render

def main(request):
    return render(request, 'home.html')

def upload1(request):
    return render(request,'upload1.html')

def upload2(request):
    return render(request,'upload2.html')

def upload3(request):
    return render(request,'upload3.html')