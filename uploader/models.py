from django.db import models
from django.dispatch import receiver
import os

from .utils import generate_random_folder


class UploadFile(models.Model):
    filename = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to=generate_random_folder)
    downloads = models.IntegerField(default=0)
    uploaded_on = models.DateTimeField(auto_now_add=True, blank=True)
    last_accessed_on = models.DateTimeField(auto_now_add=True, blank=True)

    def get_file_url(self, request):
        return 'http://' + request.META['HTTP_HOST'] + '/view_file/{}'.format(self.id)

    def get_download_url(self, request):
        return 'http://' + request.META['HTTP_HOST'] + '/download/{}'.format(self.id)


@receiver(models.signals.post_delete, sender=UploadFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `UploadFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
