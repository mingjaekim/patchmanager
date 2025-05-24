from django.contrib import admin
from .models import Patch

@admin.register(Patch)
class PatchAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'author', 'zip_name', 'description')  # 표에 보일 항목
    search_fields = ('author', 'zip_name', 'description')
    ordering = ('-created_at',)
