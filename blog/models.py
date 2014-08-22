from django.db import models
from django.utils import timezone

import datetime

# Representa el modelo de una entrada en el blog
class Entrada(models.Model):
    # Titulo de la entrada
    titulo = models.CharField('titulo', max_length=150)
    # Descripcion
    descripcion = models.CharField('descripcion', max_length=150)
    # Texto de la publicacion
    contenido = models.TextField('contenido')
    # Fecha de publicacion, por defecto toma la hora en el momento
    fecha_pub = models.DateTimeField('fecha de publicacion', default=timezone.now())
    
    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return self.titulo
    
    # Fue publicado recientemente? Devuelve True o False
    def publicacion_reciente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.fecha_pub < now

    publicacion_reciente.admin_order_field = 'fecha_pub'
    publicacion_reciente.boolean = True
    publicacion_reciente.short_description = 'Fue publicado recientemente?'

# Representa el modelo de un comentario en alguna de las entradas del blog
class Comentario(models.Model):
    # Se asocia a una entrada
    entrada = models.ForeignKey(Entrada)
    # Nombre del autor del comentario
    autor = models.CharField('autor', max_length=150, default='- anonimo -')
    # Texto del comentario
    comentario = models.TextField('comentario', max_length=400)
    # Fecha de publicacion, por defecto toma la hora en el momento
    fecha_pub = models.DateTimeField('fecha de publicacion', default=timezone.now())

    # Similar a __str__, devuelve una descripcion mas amigable
    def __unicode__(self):
        return 'Comentado por: ' + self.autor




