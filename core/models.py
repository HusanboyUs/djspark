from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django_cleanup.signals import cleanup_pre_delete   
from datetime import datetime, timedelta


class FileModel(models.Model):
    title=models.CharField(default='brokenData',max_length=10,null=True,blank=True)
    mode_choice=(
        ('ALL','ALL'),
        ('ANY','ANY'),
        ('NONE','NONE'),

    )
    mode=models.CharField(choices=mode_choice,default='Choose Mode',max_length=40)
    subset=models.CharField(max_length=100,null=True,blank=True)
    file=models.FileField(upload_to='uploads/')
    created=models.DateTimeField(auto_now_add=True)
    expires_at = datetime.now() + timedelta(minutes=5)

   



  

