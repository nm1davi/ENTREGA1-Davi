from django import forms

class FormPerro(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacio = forms.DateField(required=False)
    