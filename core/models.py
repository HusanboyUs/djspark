from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
  



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
    schema=models.TextField(max_length=10000,editable=True,null=True,blank=True)
    

   



  

