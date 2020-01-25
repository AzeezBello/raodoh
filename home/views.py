from django.shortcuts import render


# Create your views here.
def index(request):

    return render(request, 'home/index.html', {})


def thanks(request):

    return render(request, 'home/thanks.html', {})

def signup(request):

    return render(request, 'registration/signup.html', {})