from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.image_upload, name='upload')
]