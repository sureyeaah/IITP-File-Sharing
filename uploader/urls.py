from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('download/<str:id>/', views.download, name='download'),
    path('view_file/<str:id>/', views.view_file, name='view_file'),
    path('all_files/', views.all_files, name='all_files'),
    path('recent_files/', views.recent_files, name='recent_files')
]
