from django.forms import ModelForm
from .models import Lesson


class LessonForm(ModelForm):
    class Meta:
        model = Lesson
        fields = ('title', 'course', 'body', 'url', 'video')

