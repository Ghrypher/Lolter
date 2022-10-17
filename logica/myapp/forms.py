from django import forms

class buscar(forms.Form):
    busqueda=forms.CharField(label="busqueda", widget=forms.Textarea,required=False)