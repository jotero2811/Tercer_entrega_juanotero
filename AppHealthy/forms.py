from django import forms

class FrutosecoFormulario(forms.Form):
    nombre=forms.CharField()
    presentacion=forms.CharField()
    precio=forms.FloatField()
    
class SemillaFormulario(forms.Form):
    nombre=forms.CharField()
    presentacion=forms.CharField()
    precio=forms.FloatField()

class EspeciaFormulario(forms.Form):
    nombre=forms.CharField()
    presentacion=forms.CharField()
    precio=forms.FloatField()