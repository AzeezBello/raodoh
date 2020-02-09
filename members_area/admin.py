from django.contrib import admin
from .models import Course, Lesson, Comment, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'video_url', 'create_time', 'last_modified']


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment, CommentAdmin)

