from django.shortcuts import render


# Create your views here.
def members_area(request):

    return render(request, 'members_area/index.html', {})


def dashboard(request):

    return render(request, 'members_area/dashboard.html', {})

