
# Aqui es donde tendremos todos los datos de las BD
from django.db import models
from django.utils import timezone       # 6 paso
import datetime


# Definimos dos clases

# Las clases siempre en singular .... y hereda la clase model de Django que viene de models de la importacion
# Atributos ( corresponden a las columnas de la tabla question )
# Se recalca que Django automaticamente ya define las id ( no lo tenemos que hace nosotros ) pero si creamos el resto de columnas


# Creamos el primer modelo      1 paso
class Question(models.Model):           # Clase
    # id                                # Atributos 
    question_text = models.CharField(max_length=200)           # Tipo de dato Varchar con 200 caracteres                 
    pub_date = models.DateTimeField("date published")          # Tipo de dato tiempo y fecha y parametro como nombre para entender de que se trata   
                                                                                                                    # en este caso fecha publicada

    # Despues de hacer algunas pruebas en la consola crearemos el siguiente metodo

    def __str__(self):      # 3 paso
        return self.question_text       # Cada vez que invoquemos un objeto de tipo question en la consola o en cualquier parte del codigo
                                        # lo que queremos que django nos muestre es el question_text (el valor del texto que tiene la perunta) 

                                        # Luego hacemos lo mismo con Choice
    

    # Mas adelante creamos otro metodo 
                        # 5 paso
    def was_published_recently(self):   # Este metodo retorna V o F si la pregunta fue publicada recientemente
        # Me doy cuenta que la pregunta fue publicada recientemente, si tiene maximo 1 dia de antiguedad
                    # Entonces aprovechamos para importar la libreria time zone
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)        # timedeleta define diferencia de tiempo
                                # Le restamos al tiempo actual un dia
        


# Creamos el segundo modelo
class Choice(models.Model):         # 2 paso
    question = models.ForeignKey(Question,on_delete=models.CASCADE)     
                # Llave foranea que conecta la relacion con la tabla Question, y agregamos el parametro para borrar 
                # (cada vez que borremos una pregunta se van a borrar en cascada todas las Choices que esa pregunta tenga)   Para seleccion multiple

    choice_text = models.CharField(max_length=200)              # Tipo de dato Varchar
    votes = models.IntegerField(default=0)                      # Tipo de dato Integer
                # Donde se llevara la cuenta de cuantos votos tienen cada una de las respuestas
                # Sera un contador que empezara en cero y se incrementara poco a poco mientras nosotros hacemos la app
    

    def __str__(self):      # 4 paso
        return self.choice_text