from django import forms
from .models import Image, Feedback
from django.forms.widgets import RangeInput

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'body')

class DataForm(forms.Form):
    horizontal_flip = forms.IntegerField(widget=RangeInput)
    vertical_flip = forms.IntegerField(widget=RangeInput)
    grayscale = forms.IntegerField(widget=RangeInput)
    sepia = forms.IntegerField(widget=RangeInput)
    binarize = forms.IntegerField(widget=RangeInput)
    smoothness = forms.IntegerField(widget=RangeInput)
    sharpness = forms.IntegerField(widget=RangeInput)
    brightness = forms.IntegerField(widget=RangeInput)
    contrast = forms.IntegerField(widget=RangeInput)
    saturation = forms.IntegerField(widget=RangeInput)
    resize = forms.IntegerField(widget=RangeInput)