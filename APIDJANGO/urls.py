"""APIDJANGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include 
from django.contrib import staticfiles
from api.views import UserFormView
from api.views import EncuestaFormView
from api.views import Home
from api.views import Registro
from api.views import Index
from api.views import Graficas
from api.views import Encuesta
from api.views import Formulario
from api.views import LoginView 
from django.views.generic import TemplateView 




urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Url de ruta
    path('', Home.as_view(),name='login'),
    path('Registro/',Registro.as_view(),name='Registro'),
    path('index/',Index.as_view(),name='Index'),
    path('graficas/',Graficas.as_view(),name='graficas'),
    path('Formulario/',Formulario.as_view(),name='Formulario'),
    path('Encuesta/',Encuesta.as_view(),name='Encuesta'),
    path('procesar_registro/',UserFormView.as_view(),name='procesar_registro'),     
    path('login/', LoginView.as_view(), name='loginview'),   
  
                                    
]
