from django.contrib import admin
from .models import JobApplication, JobPosting

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'job_type', 'is_active', 'posted_date')
    list_filter = ('job_type', 'department', 'is_active')
    search_fields = ('title', 'description', 'requirements')
    list_editable = ('is_active',)
    ordering = ('-posted_date',)


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'role', 'applied_at')
    list_filter = ('applied_at', 'job')
    search_fields = ('name', 'mobile')
    readonly_fields = ('applied_at',)
    ordering = ('-applied_at',)

    @admin.display(description='Applied For')
    def role(self, obj):
        return obj.job.title if obj.job else 'General Application'
