from django import forms
from .models import Meter, MeterData


class MeterForm(forms.ModelForm):
    class Meta:
        model = Meter
        fields = ("address",
                  "category",
                  "type",
                  "serial_num",
                  )


class MeterDataForm(forms.ModelForm):
    class Meta:
        model = MeterData
        fields = ("meter",
                  "data",
                  )
