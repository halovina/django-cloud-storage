from django.urls import path

from . import views

urlpatterns = [
    path('upload-image', views.FormUploadImage.as_view(), name='form_upload'),
]