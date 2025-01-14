from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.conf import settings
from google.cloud import storage
from django.contrib import messages

# Create your views here.
class FormUploadImage(TemplateView):
    template_name = "home/formupload.html"
    
    def post(self, request, *args, **kwargs):
        
        if 'uploaded_file' not in request.FILES:
            messages.error(request, "Tidak ada file yang diunggah.")
            return redirect('/home/upload-image')

        image = request.FILES['uploaded_file']
        
        # Buat client untuk berinteraksi dengan Google Cloud Storage
        storage_client = storage.Client()
        bucket = storage_client.bucket(settings.BUCKET_NAME)
        blob = bucket.blob(image.name)

        # Unggah file ke Google Cloud Storage
        blob.upload_from_file(image)
        
        messages.success(request, "Upload File sukses.")
        return redirect('/home/upload-image')  