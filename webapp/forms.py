from django import forms
from .models import *

class AddMaterial(forms.ModelForm):
    class Meta:
        model=Material
        fields='__all__'


class AddHead(forms.ModelForm):
    class Meta:
        model=Head
        fields='__all__'


# class Pressure_choice(forms.Form):
#         CHOICES = (('1', 'Internal Pressure',), ('2', 'External Pressure',))
#         choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

class Internal_Pressure(forms.Form):

        # case fixed materials
        # Material_choice = [
        #         ('1','ASME SA285 C'),
        #         ('ASME SA516','ASME SA516'),
        #         ('ASME SA537','ASME SA537'),
        #         ('Enter custom material stress','Enter custom material stress'),
        #         ]
        # but now we use from database
        Material = forms.FloatField(
        widget=forms.Select(
                choices=Material.objects.all().values_list('pk', 'Name')
                )
        )
        Custom_stress = forms.FloatField(help_text='(only used if custom stress value is entered - ignores selected material)', required=False)
        Pressure = forms.FloatField(help_text='(Pressure in KPa)')
        Outer_radius = forms.FloatField(help_text='in mm')
        Joint_efficiency= forms.FloatField()
        Corrosion= forms.FloatField(help_text='(Corrosion allowance in mm)')

class External_Pressure(forms.Form):
        Material = forms.FloatField(
        widget=forms.Select(
                choices=Material.objects.all().values_list('pk', 'Name')
                )
        )
        Head = forms.CharField(
        widget=forms.Select(
                choices=Head.objects.all().values_list('pk', 'Name')
                )
        )
        Custom_stress = forms.FloatField(help_text='(only used if custom stress value is entered - ignores selected material)', required=False)
        Pressure = forms.FloatField(help_text='(Pressure in KPa)')
        Tan_to_Tan_Length = forms.FloatField(help_text='(Tangent to Tangent Length in mm)')
        Outside_Diameter = forms.FloatField(help_text='(Outside Diameter in mm)')
        Thickness = forms.FloatField(help_text='(Initialize thickness value in mm)')
        Step_size = forms.FloatField(help_text='(Thickness iteration size in mm)')
        Temperature = forms.FloatField(help_text='(Temperature in Celsius)')
        #etc..
