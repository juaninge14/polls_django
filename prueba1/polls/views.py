#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect            # Importamos el protocolo http en su respuesta
from django.urls import reverse

from .models import Question, Choice


from django.views import generic                    # Importamos generic para poder instanciar nuestras vistas basadas en clases y no en funciones


def index(request):             # Creamos la funcion para establecer la solicitud http

    latest_question_list = Question.objects.all()       # Lo vimos en la consola de comando cuando se agrego la informacion (aqui se guardan las preguntas hechas aquella vez)
    #return HttpResponse("Estas en la pagina principal de este proyecto")
    context = {latest_question_list: latest_question_list}
    return render(request, "polls/index.html", context)          # Accede a esa ruta para mostrar lo programado en las views

# Para ver este (hola a todos) debemos irnos al archivo urls.py del directorio raiz (asgi, wsgi, settings, urls)





# Crearemos las siguientes vistas

"""
def detail(request,question_id):                    # Recibe el paramtero request siempre (por el protocolo http para luego procesar y responder) 
                                                    # y recibe un parametro que tendra la id de la tabla question creada en el models

    #question = Question.objects.get(pk=question_id)     # Estos es valido, pero si no encontramos el contenido de esa id vamos a tener un error (404)              # importamos get_objects_or_404
    question = get_object_or_404(Question, pk=question_id)         # Hace lo mismo pero django automaicamente eleva el error 404 por nosotros
        # los parametros son el modelo a partir del cual nosotros vamos a buscar y el valor a partir del cual vamos a ejecutar internamente la funcion get (ese valor sera la pk)
    return render(request,"polls/detail2.html", {"question":question})

    #return HttpResponse(f"Estas viendo la pregunta N° {question_id}")       # Se le muestra al usuario


def results(request,question_id):
    # return HttpResponse(f"Estas viendo los resultados de la pregunta N° {question_id}") 
    question = get_object_or_404(Question, pk =question_id) 
    return render(request, "polls/results.html", {"question": question,})
"""


def vote(request,question_id):      # Recibe estos 2 parametros que vienen de detail2.html      donde cada vez que se envie un formulario se le envia a esta vista una request o question_id
    # return HttpResponse(f"Estas votando a la pregunta N° {question_id}") 
    question = get_object_or_404(Question, pk = question_id)
    # primero obtenemos la pregunta

    # Ahora hacemos un try excepet, porque intentamos ibtener la respuesta del usuario
    # si la respuesta del usuario existe van a pasar las cosas que estan despues del else, si no exsite va a pasar lo del except. 

    try:
        select_choice = question.choice_set.get(pk=request.POST["choice"])      # Choice hace referencia al name que se puso en el input de detail.html
                                                                                # En DJando podemos recuperar un valor de un formulario en una vista de la siguiente manera: request.POST["nombreDelInput"]
    except (KeyError,Choice.DoesNotExist) :
        return render(request,"polls/detail2.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        select_choice.vote =+ 1
        select_choice.save()
        return HttpResponseRedirect(reverse("polls:result",args = (question.id,) ))

# Para ver estas vistas, tenemos que modificar el archivo urls.py de la app (polls)



# Luego de lo anterior, podemos ligarlas a un template (Front-end) 
# Nos dirigimos a la carpeta donde estamos trabajando --- app(polls) cremos una carpeta nueva y le vamos a nombrar (templates) y dentro de templates crearemos las carpetas de las aplicaciones
# con los mismos nombres para tener el orden de lo hecho en el back con ahora el front (en este caso carpeta polls) y dentro de ella empezamos a crear las templates en (HTML y front ...)





# Ahora crearemos vistas basadas en clases


# Con la siguiente clase hacemos exactamente lo mismo que hacia con la funcion index pero mas sencilla y entendible   ( No se necesita trabajar con elr render)
class IndexView(generic.ListView):                      # Primera generic view
    template_new = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Return the last five published questions 
        return Question.objects.order_by("-pub_date") [:5]                   # Order_ by es igual quefilter con la diferencia que me permite generar el orden de como quiero ver las respuestas 
                                                                        # - pub_date me indica que voy a traer las preguntas ordenadas desde las mas recientes hasta las mas antiguas


class DetailView(generic.DeleteView):
    model = Question
    template_name = "polls/detail.html"



class ResultView(generic.DeleteView):
    model = Question
    template_name = "polls/results.html"



# Ahora vamos al archivo urls.py y en lugar de llamar a las funciones 







# En que momento utilizar las functions o las class?

# Cuando cargo datos de la BD genero un template y lo muestro, usamos Generic Views o sea (Class Based Views)
# Si es mas complejo como mostrar 2 formularios en una misma pagina, usamos Functions views


                    # SIEMPRE,  intentar Generic views, si no se puede entonces Function views