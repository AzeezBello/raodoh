from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('thanks/', views.thanks, name='thanks'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit-profile'),
    path('upload/', views.upload, name='upload'),
    path('activation_sent/', views.activation_sent, name='activation_sent'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
