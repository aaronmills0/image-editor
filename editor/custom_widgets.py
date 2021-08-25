from django.forms.widgets import NumberInput

class RangeInput(NumberInput):
    input_type ='range'

class SwitchInput(NumberInput):
    input_type ='switch'