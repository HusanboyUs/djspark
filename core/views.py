from django.shortcuts import render,redirect
from .cleaner import SparkApp
import os
from .forms import FileUploadForm
from .models import FileModel
# Create your views here.
from django.conf import settings

def mainPage(request):
    context = None
    form=FileUploadForm()
    latest_file=FileModel.objects.order_by('id').first()
    file_path = os.path.join(settings.MEDIA_ROOT, latest_file.file.name)


    
    result=SparkApp(file_path).cleanAll()
        
        


    
    return render(request,'main/main.html',{'form':form,'dataframe':result})



