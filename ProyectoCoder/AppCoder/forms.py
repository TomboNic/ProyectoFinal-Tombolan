from django import forms

class FutbolFormulario(forms.Form):
    Nombre = forms.CharField()
    equipo = forms.CharField()

class VoleyFormulario(forms.Form):
    Nombre = forms.CharField()
    equipo = forms.CharField()

class Formula1Formulario(forms.Form):
    Nombre = forms.CharField()
    equipo = forms.CharField()

class BasquetFormulario(forms.Form):
    Nombre = forms.CharField()
    equipo = forms.CharField()