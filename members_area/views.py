from django.shortcuts import render
from .models import Course, Lesson


# Create your views here.
def members_area(request):
    courses = Course.objects.all()
    print(courses)
    lessons = Course.objects.all().prefetch_related('lessons')
    # print(lessons)
    context = {
        "courses": courses,
        "lessons": lessons,
    }

    return render(request, 'members_area/index.html', context)


def dashboard(request):

    return render(request, 'members_area/dashboard.html', {})


def lesson(request, pk):
    lessons = Lesson.objects.get(pk=pk)

    context = {
        "lessons": lessons,
    }

    return render(request, "members_area/lesson.html", context)