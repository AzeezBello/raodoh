from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField("Title", max_length=150, blank=True)
    category = models.ManyToManyField('Category')
    create_time = models.DateTimeField(auto_now_add=True)
    # lessons =

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField("Title", max_length=250, blank=True)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE, null=True)
    body = models.TextField()
    video_url = models.URLField(max_length=350, blank=True, null=True)
    resources = models.FileField(upload_to='resources/', null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.author
