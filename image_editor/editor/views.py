from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
import cv2 as cv
import numpy as np
from PIL import Image
import os, shutil
from django.conf import settings
# Create your views here.
img_name = None;

def clear_tmp():
    folder = settings.MEDIA_ROOT + 'tmp'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to clear /tmp: {}".format(e))

def image_upload(request):
    clear_tmp()
    global img_name
    print(request.method)
    template_name ='index.html'
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            print(form)
            print(img)
            img.save()
            img_name = form.cleaned_data.get('image')
            print(img_name)
            return redirect('/canvas/')
    else:
        form = ImageForm()
    return render(request, template_name, {'form': form})


def canvas(request):
    template_name = 'canvas.html'
    print('Name: {}'.format(img_name))
    return render(request, template_name, {'name': img_name})