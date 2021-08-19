from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm, DataForm
import cv2 as cv
import numpy as np
from PIL import Image
import os, shutil
from django.conf import settings
from .editor import Editor
# Create your views here.
img_name = None
img_copy_name = None
temp = {
    "grayscale": 0,
    "sepia": 0,
    "binarize": 0,
    "smoothness": 0,
    "sharpness": 0,
    "brightness": 0,
    "contrast": 0,
    "saturation": 0,
    "resize": 0
}

def clear_tmp():
    global temp
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
    temp = {
        "grayscale": 0,
        "sepia": 0,
        "binarize": 0,
        "smoothness": 0,
        "sharpness": 0,
        "brightness": 0,
        "contrast": 0,
        "saturation": 0,
        "resize": 0
    }

def copy_img(name):
    global img_copy_name
    folder = settings.MEDIA_ROOT + 'tmp'
    index = str(name).find('.')
    new_name = str(name)[:index] + '_copy' + str(name)[index:]
    img_copy_name = new_name
    print("New name: {}".format(new_name))
    try:
        original = os.path.join(folder, str(name))
        copy = os.path.join(folder, new_name)
        shutil.copy(original, copy)
    except Exception as e:
        print("Failed to copy {}".format(name))
        


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
            copy_img(img_name)
            print(img_name)
            return redirect('/canvas/')
    else:
        form = ImageForm()
    return render(request, template_name, {'form': form})

def canvas(request):
    global temp
    template_name = 'canvas.html'
    print('Name: {}'.format(img_name))
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = {}
            data.update({"grayscale": form.cleaned_data.get("grayscale")})
            data.update({"sepia": form.cleaned_data.get("sepia")})
            data.update({"binarize": form.cleaned_data.get("binarize")})
            data.update({"smoothness": form.cleaned_data.get("smoothness")})
            data.update({"sharpness": form.cleaned_data.get("sharpness")})
            data.update({"brightness": form.cleaned_data.get("brightness")})
            data.update({"contrast": form.cleaned_data.get("contrast")})
            data.update({"saturation": form.cleaned_data.get("saturation")})
            data.update({"resize": form.cleaned_data.get("resize")})
            temp = data.copy()
            print("Data: {}".format(data))
            print("Temp: {}".format(temp))
            editor = Editor(temp)
            editor.update()
        else: 
            print("Invalid form")
    else:
        print("Form: {}".format(temp))
        form = DataForm()
    res = {
        'name': img_name, 
        'form': form, 
        'grayscale': temp.get('grayscale'),
        'sepia': temp.get('sepia'),
        'binarize': temp.get('binarize'),
        'smoothness': temp.get('smoothness'),
        'sharpness': temp.get('sharpness'),
        'brightness': temp.get('brightness'),
        'contrast': temp.get('contrast'),
        'saturation': temp.get('saturation'),
        'resize': temp.get('resize')
        }
    print("Res: {}".format(res))
    return render(request, template_name, res)