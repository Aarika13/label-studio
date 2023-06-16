from django.urls import path
from .views import download_file

urlpatterns = [
    path('download/', download_file, name='download_file'),
]
