from django.contrib import admin
from .models import Course, Lesson, Comment, Category


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    pass


class LessonAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CommentAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)


