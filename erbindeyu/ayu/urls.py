from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('music/', views.music, name="music"),
    path('vlog/', views.vlog, name="vlog"),
    # Add the remaining URL path configurations here
    path('photo/', views.photo, name="photo"),
    path('love/', views.love, name="love"),
]
