from django.db import models
from django_cleanup import cleanup
from datetime import datetime, timedelta


class FileModel(models.Model):
    title=models.CharField(default='data1',max_length=10,null=True,blank=True)
    file=models.FileField(upload_to='uploads/')
    created=models.DateTimeField(auto_now_add=True)
    expires_at = datetime.now() + timedelta(minutes=5)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()  # Delete the associated file
        super().delete(*args, **kwargs)

  

