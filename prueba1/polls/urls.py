
# Se creo este archivo luego de haber puesto la url en el archivo urls de la carpeta raiz de django (directorio de archivos)


from django.urls import path        

from . import views         # Importamos algo del paquete actual en donde esta este archivo (paquete = polls,  el archivo views )


# De views usaremos 

app_name = "polls"              # Para evitar el hard coding   (tener direccion sin hardcoding a todos los archivos html) y en los archivos .html trabajamos con la etiqueta url
# Nombre de la app con la que nos vamos a quedar para referenciar los archivos
# Esto se hace por si yo quiero cambiar el nombre de una url o la url en si, django lo pueda hacer para todas y no me toque hacerlo uno a uno (porque puedo tener muchos templates para modificar)

"""
urlpatterns = [
    path("", views.index, name="index"),     # str vacio, la funcion index creada en el archivo views (siempre muestra la pagina principal)
                                            # y un atributo name que tiene un nombre descriptico de esa ruta (name=index)
    # Luego de crear las vistas (funciones) en views.py agregamos las sigueintes rutas

        # ej: /polls/5                                              # Este numero entero (5) es el que pasara como argumento o paramtero en la funcion detail
    path("<int:question_id>/detail/", views.detail, name="detail"),
        # ej: /polls/5/results                                                                                                         # en la funcion detail
    path("<int:question_id>/results/", views.results, name="results"),
        # # ej: /polls/5/vote                                                                                                          # en la funcion vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
"""

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),                                  # Forma de correr el template renderizado que corresponde a esta vista                          
    path("<int:pk>/detail2/", views.ResultView.as_view(), name="detail"),                                                                                                              
    path("<int:pk>/results/", views.DetailView.as_view(), name="results"),               # con el pk django sabe que el parametro que llega es una pk y puede buscar en los modelos question a la pregunta que yo necesito                                                                                      
    path("<int:question_id>/vote/", views.vote, name="vote")                            # Esta queda tal cual porque esta creada a traves de una function view y no de una class based views
]