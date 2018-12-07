from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import UploadForm
from .models import UploadFile
from .utils import send_email
from datetime import datetime


def home(request):
    return render(request, 'uploader/upload.html', {})


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES or None)
        if form.is_valid():
            new_file = UploadFile(file=request.FILES['file'])
            new_file.filename = new_file.file.name
            new_file.save()
            file_url = new_file.get_file_url(request)
            print(file_url)
            return redirect(file_url)
    return redirect('/')

def view_file(request, id):
    obj = get_object_or_404(UploadFile, id=id)
    download_url = obj.get_download_url(request)
    return render(request, 'uploader/view_file.html', {'obj': obj, 'download_url': download_url})


def download(request, id):
    obj = get_object_or_404(UploadFile, id=id)

    obj.downloads = obj.downloads + 1
    obj.last_accessed_on = datetime.now()
    obj.save()

    filename = obj.file.name.split('/')[-1]
    response = HttpResponse(obj.file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response


def all_files(request):
    query_results = UploadFile.objects.all()
    for item in query_results:
        item.url = item.get_file_url(request)
    return render(request, 'uploader/view_files.html', {'query_results': query_results})


def recent_files(request):
    query_results = UploadFile.objects.order_by('-uploaded_on')[:15]
    for item in query_results:
        item.url = item.get_file_url(request)
    return render(request, 'uploader/view_files.html', {'query_results': query_results})
