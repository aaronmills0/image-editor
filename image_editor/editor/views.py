from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm
import cv2 as cv
import numpy as np
from PIL import Image
# Create your views here.
img_name = None;

def image_upload(request):
    print(request.method)
    template_name ='index.html'
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            print(form)
            print(img)
            img.save()
            img_name = img
            return redirect('/canvas/')
    else:
        form = ImageForm()
    return render(request, template_name, {'form': form})


def canvas(request):
    template_name = 'canvas.html'
    return render(request, template_name, {'name': img_name})