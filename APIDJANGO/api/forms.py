from django import forms
from .models import User
from .models import Encuesta 
from django.forms import ModelForm

class RegistroForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Name','password','email']
        
class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['Name','Area','pregunta1','Pregunta2','Pregunta3','Pregunta4','Pregunta5','Pregunta6','Pregunta7','Pregunta8','Pregunta9','Pregunta10','Pregunta11']
        