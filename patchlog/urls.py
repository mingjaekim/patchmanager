from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_patch, name='upload_patch'),
    path('success/', views.upload_success, name='upload_success'),
    path('history/', views.upload_history, name='upload_history'),
]
