from django.shortcuts import render,redirect
from .cleaner import SparkApp
import os
from .forms import FileUploadForm
from .models import FileModel
from django.conf import settings
from django.http import HttpResponse
import multiprocessing

def mainPage(request):
    latest_file = None
    form=FileUploadForm()
    
    if request.method == 'POST':
        form=FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 

         

        latest_file=FileModel.objects.order_by('id').first()
        #file_path = os.path.join(settings.MEDIA_ROOT, latest_file.file.name)
        #result=SparkApp(file_path).cleanAny()
             


    
    return render(request,'main/form.html',{'form':form,'dataframe':latest_file,'file':latest_file})



def listFiles(request):
    files=FileModel.objects.all()
    context={'files':files}
    return render(request,'main/list.html',context)


def viewPage(request,pk):
    file=FileModel.objects.get(id=pk)
    file_path=os.path.join(settings.MEDIA_ROOT,file.file.name)
    print(file.mode)
    machine=SparkApp(file_path)
    if file.mode == 'ALL':
        result=machine.cleanAll()
        schema=machine.recommendSchema()
     
    else:
        result=machine.cleanAny()
        schema=machine.recommendSchema()

    
    
    print('schema is saved! --------------')

   
    context={'result':result,'schema':schema,'file':file}
    return render(request,'main/live.html',context)        





def deletePage(request,pk):
    file=FileModel.objects.get(id=pk)
    file.delete()
    return redirect('listPage')

def downloadPage(request,pk):
    file=FileModel.objects.get(id=pk)
    file_path=os.path.join(settings.MEDIA_ROOT,file.file.name)
    if request.method == 'GET':
        file_path = file.file.path
        with open(file_path, 'rb') as file:
        # Set the appropriate content-type and headers for the response
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'

        return response     


