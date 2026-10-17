from django.urls import path

from . import views

urlpatterns = [
    path('', views.career, name='career'),
    path('apply/', views.apply, name='career_apply'),
    path('apply/<int:job_id>/', views.apply, name='career_apply_job'),
]
