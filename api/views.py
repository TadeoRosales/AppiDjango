from django.shortcuts import render
from rest_framework .views import APIView
from django.shortcuts import redirect, render 
from django.contrib.auth import authenticate, login 
from django.core.mail import send_mail 
from django.conf import settings
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
from .forms import RegistroForms
from .models import Encuesta
from .models import User 
from .forms import EncuestaForm





# Create your views here.
class Home(APIView):
    template_name='login.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Registro(APIView):
    template_name='Registro.html'
    def get(self,request):
        return render(request,self.template_name)

class Index(APIView):
    template_name='Index.html'
    def get(self,request):
        return render(request,self.template_name)
    
class Formulario(APIView):
    template_name='Formulario.html'
    def get(self,request):
        return render(request,self.template_name)    
      
class Encuesta(APIView):
    template_name='Encuesta.html'
    def get(self,request):
        return render(request,self.template_name)
      
class Analisis(APIView):
    template_name='Analisis.html'
    def get(self,request):
        return render(request,self.template_name)
    


class UserFormView(APIView):
  template_name:'Registro.html' #Buscar paguina de html
    
  def post(self, request):
    form = RegistroForms(request.POST)
    if form.is_valid():
      user = form.save()
      
      #Mandar correo
      subject = 'Confirmacion de Registro'
      message = 'Tu registro fue exitoso'
      message += f'\nNombre: {user.Name}'
      message += f'\nNombre: {user.password}'
      message += f'\nNombre: {user.email}'
      
      from_email = settings.EMAIL_HOST_USER
      recipient_list = [user.email] #Usar el correo del usuario
      
      
      #Enviar correo
      send_mail(
        subject, message, from_email, recipient_list,
        fail_silently=False,
      )
      
      return redirect('login')
    
    return render(request, self.template_name,{'form':form})
  
  
class LoginView(APIView):
   template_name = 'Index.html' #Plantilla de inicio de sesion
   
   def get (self,request):
     return render (request, self.template_name)
   
   def post (self, request):
     email = request.POST.get('email')
     password = request.POST.get('password')
     
     #consulta a los usuarios ingresados en la base de datos
     try:
       user=User.objects.get(email=email, password=password)
     except User.DoesNotExist:
       user=None
       
     if user is not None:
        return redirect('Formulario')
     else:
        return render(request,self.template_name,{'error_message':'Datos invalidos Intentalo nuevamente'})
        
    
class EncuestaFormView(APIView):
  template_name='Encuesta.html' #Buscar paguina de html
    
  def post(self, request):
    form = EncuestaForm(request.POST)
    if form.is_valid():
      user = form.save()
      
      return redirect('login')
    
    return render(request, self.template_name,{'form':form})
  

from rest_framework.response import Response
from django.shortcuts import render
from .models import Datoscsv

class Graficas(APIView):
    def get(self, request):
        datos = Datoscsv.objects.all()

        # Procesa los datos para contar las respuestas a "pregunta1"
        respuestas_pregunta1 = {}
        for dato in datos:
            respuesta = dato.pregunta1
            if respuesta in respuestas_pregunta1:
                respuestas_pregunta1[respuesta] += 1
                
            else:
                respuestas_pregunta1[respuesta] = 1

        # Procesa los datos para contar las respuestas a "pregunta2"
        respuestas_pregunta2 = {}
        for dato in datos:
            respuesta = dato.Pregunta2
            if respuesta in respuestas_pregunta2:
                respuestas_pregunta2[respuesta] += 1
            else:
                respuestas_pregunta2[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta3"
        respuestas_pregunta3 = {}
        for dato in datos:
            respuesta = dato.Pregunta3
            if respuesta in respuestas_pregunta3:
                respuestas_pregunta3[respuesta] += 1
            else:
                respuestas_pregunta3[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta4"
        respuestas_pregunta4 = {}
        for dato in datos:
            respuesta = dato.Pregunta4
            if respuesta in respuestas_pregunta4:
                respuestas_pregunta4[respuesta] += 1
            else:
                respuestas_pregunta4[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta5"
        respuestas_pregunta5 = {}
        for dato in datos:
            respuesta = dato.Pregunta5
            if respuesta in respuestas_pregunta5:
                respuestas_pregunta5[respuesta] += 1
            else:
                respuestas_pregunta5[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta6"
        respuestas_pregunta6 = {}
        for dato in datos:
            respuesta = dato.Pregunta6
            if respuesta in respuestas_pregunta6:
                respuestas_pregunta6[respuesta] += 1
            else:
                respuestas_pregunta6[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta7"
        respuestas_pregunta7 = {}
        for dato in datos:
            respuesta = dato.Pregunta7
            if respuesta in respuestas_pregunta7:
                respuestas_pregunta7[respuesta] += 1
            else:
                respuestas_pregunta7[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta8"
        respuestas_pregunta8 = {}
        for dato in datos:
            respuesta = dato.Pregunta8
            if respuesta in respuestas_pregunta8:
                respuestas_pregunta8[respuesta] += 1
            else:
                respuestas_pregunta8[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta9"
        respuestas_pregunta9 = {}
        for dato in datos:
            respuesta = dato.Pregunta9
            if respuesta in respuestas_pregunta9:
                respuestas_pregunta9[respuesta] += 1
            else:
                respuestas_pregunta9[respuesta] = 1
        # Procesa los datos para contar las respuestas a "pregunta10"
        respuestas_pregunta10 = {}
        for dato in datos:
            respuesta = dato.Pregunta10
            if respuesta in respuestas_pregunta10:
                respuestas_pregunta10[respuesta] += 1
            else:
                respuestas_pregunta10[respuesta] = 1

        # Prepara los datos en un formato adecuado para los gráficos
        labels_pregunta1 = list(respuestas_pregunta1.keys())
        data_pregunta1 = list(respuestas_pregunta1.values())

        labels_pregunta2 = list(respuestas_pregunta2.keys())
        data_pregunta2 = list(respuestas_pregunta2.values())

        labels_pregunta3 = list(respuestas_pregunta3.keys())
        data_pregunta3 = list(respuestas_pregunta3.values())

        labels_pregunta4 = list(respuestas_pregunta4.keys())
        data_pregunta4 = list(respuestas_pregunta4.values())

        labels_pregunta5 = list(respuestas_pregunta5.keys())
        data_pregunta5 = list(respuestas_pregunta5.values())

        labels_pregunta6 = list(respuestas_pregunta6.keys())
        data_pregunta6 = list(respuestas_pregunta6.values())

        labels_pregunta7 = list(respuestas_pregunta7.keys())
        data_pregunta7 = list(respuestas_pregunta7.values())

        labels_pregunta8 = list(respuestas_pregunta8.keys())
        data_pregunta8 = list(respuestas_pregunta8.values())

        labels_pregunta9 = list(respuestas_pregunta9.keys())
        data_pregunta9 = list(respuestas_pregunta9.values())

        labels_pregunta10 = list(respuestas_pregunta10.keys())
        data_pregunta10 = list(respuestas_pregunta10.values())

        # Puedes repetir el proceso para las otras preguntas

        return render(request, 'graficas.html', {
            'labels_pregunta1': labels_pregunta1,
            'data_pregunta1': data_pregunta1,

            'labels_pregunta2': labels_pregunta2,
            'data_pregunta2': data_pregunta2,

            'labels_pregunta3': labels_pregunta3,
            'data_pregunta3': data_pregunta3,

            'labels_pregunta4': labels_pregunta4,
            'data_pregunta4': data_pregunta4,

            'labels_pregunta5': labels_pregunta5,
            'data_pregunta5': data_pregunta5,

            'labels_pregunta6': labels_pregunta6,
            'data_pregunta6': data_pregunta6,

            'labels_pregunta7': labels_pregunta7,
            'data_pregunta7': data_pregunta7,

            'labels_pregunta8': labels_pregunta8,
            'data_pregunta8': data_pregunta8,

            'labels_pregunta9': labels_pregunta9,
            'data_pregunta9': data_pregunta9,

            'labels_pregunta10': labels_pregunta10,
            'data_pregunta10': data_pregunta10,
            # Agrega aquí las variables para las otras preguntas
        })



