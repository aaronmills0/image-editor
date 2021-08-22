from django import forms
from .models import Image, Feedback
from django.forms.widgets import RangeInput, SwitchInput, NumberInput
from colorfield.widgets import ColorWidget

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'body')

class DataForm(forms.Form):
    horizontal_flip = forms.IntegerField(widget=SwitchInput)
    vertical_flip = forms.IntegerField(widget=SwitchInput)
    grayscale = forms.IntegerField(widget=SwitchInput)
    sepia = forms.IntegerField(widget=SwitchInput)
    binarize = forms.IntegerField(widget=SwitchInput)
    histogram_equalize = forms.IntegerField(widget=SwitchInput)
    invert = forms.IntegerField(widget=SwitchInput)
    smoothness = forms.IntegerField(widget=RangeInput)
    sharpness = forms.IntegerField(widget=RangeInput)
    brightness = forms.IntegerField(widget=RangeInput)
    contrast = forms.IntegerField(widget=RangeInput)
    gamma_correction = forms.IntegerField(widget=RangeInput)
    saturation = forms.IntegerField(widget=RangeInput)
    resize = forms.IntegerField(widget=RangeInput)
    color_pop_bool = forms.IntegerField(widget=SwitchInput)
    color_pop_color = forms.CharField(widget=ColorWidget)
    color_pop_data = forms.CharField(required=False)
