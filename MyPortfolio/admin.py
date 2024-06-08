# In admin.py of your portfolio app

from django.contrib import admin
from .models import Project

@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    search_fields = ('title',)

