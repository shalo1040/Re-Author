from django.shortcuts import render

def main(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')