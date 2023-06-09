from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("upload/", views.upload_file, name="upload"),
    path("download/", views.download_report, name="download")
]
