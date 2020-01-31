from django.shortcuts import render
from .models import Course, Lesson


# Create your views here.
def members_area(request):
    courses = Course.objects.all()
    print(courses)
    # print(courses.lessons.all())
    lessons = Course.lessons
    print(lessons)
    context = {
        "courses": courses,
        "lessons": lessons,
    }

    return render(request, 'members_area/index.html', context)


def dashboard(request):

    return render(request, 'members_area/dashboard.html', {})

