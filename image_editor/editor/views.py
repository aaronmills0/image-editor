from django.shortcuts import render
from .models import Image
from .forms import ImageForm
# Create your views here.

def home(request):
    template_name ='index.html'
    return render(request, template_name, {})

def image_upload(request):
    template_name ='index.html'
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.instance
            return render(request, template_name, {'form': form, 'img': img})
    else:
        form = ImageForm()
    return render(request, template_name, {'form': form})