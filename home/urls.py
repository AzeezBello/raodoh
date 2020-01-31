from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('thanks/', views.thanks, name='thanks'),
    path('upload/', views.upload, name='upload' ),
]
