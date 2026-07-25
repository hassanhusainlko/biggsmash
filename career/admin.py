from django.contrib import admin
from .models import JobPosting

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'job_type', 'is_active', 'posted_date')
    list_filter = ('job_type', 'department', 'is_active')
    search_fields = ('title', 'description', 'requirements')
    list_editable = ('is_active',)
    ordering = ('-posted_date',)
