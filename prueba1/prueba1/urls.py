"""prueba1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include       # Importamos include para incluir las nuevas rutas de las otras apps (carpetas creadas como polls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include("polls.urls"))       # Nueva ruta donde podemos ver en una vista lo que queremos de la carpeta polls (app polls)
                                                # Esto quiere decir que aqui nombraremos a los archivos urls.py de la app que se este nombrando
]
