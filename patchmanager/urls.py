from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('upload_patch')),  # ← 이 줄 추가!
    path('', include('patchlog.urls')),
]
