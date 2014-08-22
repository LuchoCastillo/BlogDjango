from django.contrib import admin
from blog.models import Entrada, Comentario

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1

# Ejemplo: cambiar de orden los campos en admin
class EntradaAdmin(admin.ModelAdmin):
    inlines = [ComentarioInline]
    
    # Informacion que se muestra en la lista
    list_display = ('titulo', 'descripcion', 'fecha_pub', 'publicacion_reciente')
    # Filtro por fecha de publicacion
    list_filter = ['fecha_pub']
    # Busqueda por titulo
    search_fields = ['titulo']
    # Tinea de tiempo
    date_hierarchy = 'fecha_pub'

admin.site.register(Entrada, EntradaAdmin)
