from django.contrib import admin
from.models import Question         # Accedemos a la carpeta actual (polls) e importamos la clase Question del modelo

admin.site.register(Question)       # Esta funcion como parametro lleva el modelo que nosotros queremos colocar disponible en el administrador para que otras personas puedan editarlo
                                    # Para probar el administrador ponemos el modelo Question
