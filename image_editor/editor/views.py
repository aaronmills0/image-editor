from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm, DataForm, FeedbackForm
import cv2 as cv
import numpy as np
import os, shutil
from django.conf import settings
from .editor import Editor
# Create your views here.
img_name = None
img_copy_name = None
temp = {
    "horizontal_flip": 0,
    "vertical_flip": 0,
    "grayscale": 0,
    "sepia": 0,
    "binarize": 0,
    "histogram_equalize": 0,
    "invert": 0,
    "smoothness": 0,
    "sharpness": 0,
    "brightness": 0,
    "contrast": 0,
    "gamma_correction": 10,
    "saturation": 0,
    "resize": 0,
    "color_pop_bool": 0,
    "color_pop_color": "#ff0946",
    "color_pop_data": "",
    "crop_bool": 0,
    "crop_data": ""
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
        "horizontal_flip": 0,
        "vertical_flip": 0,
        "grayscale": 0,
        "sepia": 0,
        "binarize": 0,
        "histogram_equalize": 0,
        "invert": 0,
        "smoothness": 0,
        "sharpness": 0,
        "brightness": 0,
        "contrast": 10,
        "gamma_correction": 10,
        "saturation": 10,
        "resize": 0,
        "color_pop_bool": 0,
        "color_pop_color": "#ff0946",
        "color_pop_data": "",
        "crop_bool": 0,
        "crop_data": ""
    }
    Image.objects.all().delete()

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
            data.update({"horizontal_flip": form.cleaned_data.get("horizontal_flip")})
            data.update({"vertical_flip": form.cleaned_data.get("vertical_flip")})
            data.update({"grayscale": form.cleaned_data.get("grayscale")})
            data.update({"sepia": form.cleaned_data.get("sepia")})
            data.update({"binarize": form.cleaned_data.get("binarize")})
            data.update({"histogram_equalize": form.cleaned_data.get("histogram_equalize")})
            data.update({"invert": form.cleaned_data.get("invert")})
            data.update({"smoothness": form.cleaned_data.get("smoothness")})
            data.update({"sharpness": form.cleaned_data.get("sharpness")})
            data.update({"brightness": form.cleaned_data.get("brightness")})
            data.update({"contrast": form.cleaned_data.get("contrast")})
            data.update({"gamma_correction": form.cleaned_data.get("gamma_correction")})
            data.update({"saturation": form.cleaned_data.get("saturation")})
            data.update({"resize": form.cleaned_data.get("resize")})
            data.update({"color_pop_bool": form.cleaned_data.get("color_pop_bool")})
            data.update({"color_pop_color": form.cleaned_data.get("color_pop_color")})
            data.update({"color_pop_data": form.cleaned_data.get("color_pop_data")})
            data.update({"crop_bool": form.cleaned_data.get("crop_bool")})
            data.update({"crop_data": form.cleaned_data.get("crop_data")})
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
        'horizontal_flip': temp.get('horizontal_flip'),
        'vertical_flip': temp.get('vertical_flip'),
        'grayscale': temp.get('grayscale'),
        'sepia': temp.get('sepia'),
        'binarize': temp.get('binarize'),
        'histogram_equalize': temp.get('histogram_equalize'),
        'invert': temp.get('invert'),
        'smoothness': temp.get('smoothness'),
        'sharpness': temp.get('sharpness'),
        'brightness': temp.get('brightness'),
        'contrast': temp.get('contrast'),
        'gamma_correction': temp.get('gamma_correction'),
        'saturation': temp.get('saturation'),
        'resize': temp.get('resize'),
        'color_pop_bool': temp.get('color_pop_bool'),
        'color_pop_color': temp.get('color_pop_color'),
        'color_pop_data': temp.get('color_pop_data'),
        'crop_bool': temp.get('crop_bool'),
        'crop_data': temp.get('crop_data')
        }
    print("Res: {}".format(res))
    return render(request, template_name, res)

def feedback(request):
    template_name = 'feedback.html'
    new_feedback = None
    if request.method == 'POST':
        feedback_form = FeedbackForm(data=request.POST)
        if feedback_form.is_valid():
            new_feedback = feedback_form.save(commit=False)
            new_feedback.save()
    else:
        feedback_form = FeedbackForm()
    
    return render(request, template_name, {'form': feedback_form, 'new_feedback': new_feedback})