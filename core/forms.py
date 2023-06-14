from django.forms import ModelForm
from .models import FileModel

class FileUploadForm(ModelForm):
    class Meta:
        model=FileModel
        fields=['title','file',]
