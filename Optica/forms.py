from django import forms

class formulario_cristales(forms.Form):
    nombre =forms.CharField(max_length=50)
    precio =forms.IntegerField()

class formulario_liquidos(forms.Form):
    nombre =forms.CharField(max_length=50)
    marca =forms.CharField(max_length=50)
    precio =forms.IntegerField()

class formulario_Marcos(forms.Form):
    nombre =forms.CharField(max_length=50)
    marca =forms.CharField(max_length=50)
    precio =forms.IntegerField()