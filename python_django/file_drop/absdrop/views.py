from unicodedata import name
from django.shortcuts import render, HttpResponse
from .forms import FileUploadForm
from .models import FileUpload
# Create your views here.

def index(request):
    if request.method=='POST':
        c_form = FileUploadForm(request.POST,request.FILES)
        if c_form.is_valid():
            name=c_form.cleaned_data['file_name']
            files = c_form.cleaned_data['files_data']
            FileUpload(file_name=name,my_file=files).save()
            return HttpResponse("File Uploaded")
        else:
            return HttpResponse("Error File Uploading")
            
    else:
        context = {
        'form':FileUploadForm()
        }
        return render(request,'index.html',context)

def show_file(request):
    all_data = FileUpload.objects.all()
    context = {
        'data':all_data
    }
    return render(request,'view.html',context)