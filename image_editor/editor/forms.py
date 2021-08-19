from django import forms
from .models import Image
from django.forms.widgets import RangeInput

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class DataForm(forms.Form):
    grayscale = forms.IntegerField(widget=RangeInput)
    sepia = forms.IntegerField(widget=RangeInput)
    binarize = forms.IntegerField(widget=RangeInput)
    smoothness = forms.IntegerField(widget=RangeInput)
    sharpness = forms.IntegerField(widget=RangeInput)
    brightness = forms.IntegerField(widget=RangeInput)
    contrast = forms.IntegerField(widget=RangeInput)
    saturation = forms.IntegerField(widget=RangeInput)
    resize = forms.IntegerField(widget=RangeInput)