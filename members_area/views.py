from django.shortcuts import render
from .models import Course, Lesson


# Create your views here.
def members_area(request):
    courses = Course.objects.all().order_by('create_time')
    print(courses)
    # sidebar_lessons = Course.objects.all().prefetch_related('lessons')
    # print(lessons)
    context = {
        "courses": courses,
        # "sidebar_lessons": sidebar_lessons,
    }

    return render(request, 'members_area/index.html', context)


def dashboard(request):

    return render(request, 'members_area/dashboard.html', {})


def lesson(request, pk):
    courses = Course.objects.all()
    lessons = Lesson.objects.get(pk=pk)

    # if request.method == 'POST':
    #     form = LessonForm(request.POST, request.FILES)
    #     context = form.instance
    #     if form.is_valid():
    #         form.save()

    context = {
        "courses": courses,
        "lessons": lessons,
    }

    return render(request, "members_area/lesson.html", context)