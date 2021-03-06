from django.urls import path
from . import views

urlpatterns = [
    path('members_area/', views.members_area, name='members_area'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('course/<int:pk>/', views.course, name='course'),
    path("lesson/<int:pk>/", views.lesson, name="lesson"),
]
