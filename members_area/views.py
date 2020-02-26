from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson


# Create your views here.
@login_required
def members_area(request):
    courses = Course.objects.all().order_by('create_time')

    context = {
        "courses": courses,
    }

    return render(request, 'members_area/index.html', context)


def dashboard(request):

    return render(request, 'members_area/dashboard.html', {})


def course(request, pk):
    courses = Course.objects.get(pk=pk)

    context = {
        "courses": courses,
    }
    return render(request, "members_area/course.html", context)


def lesson(request, pk):
    courses = Course.objects.all()
    lessons = Lesson.objects.get(pk=pk)
    # prev_lesson = lessons.get_previous_by_pk
    # next_lesson = lessons.get_next_by_pk

    context = {
        "courses": courses,
        "lessons": lessons,
        # "prev_lesson": prev_lesson,
        # "next_lesson": next_lesson,
    }
    return render(request, "members_area/lesson.html", context)

