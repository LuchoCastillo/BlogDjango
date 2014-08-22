from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView
from django.utils import timezone
from django.template import RequestContext

from blog.models import Entrada

def index(request):
    ultimas_entradas = Entrada.objects.filter(fecha_pub__lte=timezone.now).order_by('-fecha_pub')[:5]
    context = {'ultimas_entradas': ultimas_entradas}
    return render(request, 'blog/index.html', context, context_instance=RequestContext(request))

def pub(request, entrada_id):
    entrada = get_object_or_404(Entrada, pk=entrada_id)
    return render(request, 'blog/pub.html', {'entrada': entrada}, context_instance=RequestContext(request))

def comment(request, entrada_id):
    autor = request.POST['autor']
    comentario = request.POST['comentario']
    # Pido la entrada que se comento
    entrada = get_object_or_404(Entrada, pk=entrada_id)

    # Si no se ha ingresado un comentario
    if not comentario:
        mensaje = 'No se ha ingresado un comentario.'
        tipo_msj = 'danger'
    # Si se ha ingresado autor
    elif autor:
        entrada.comentario_set.create(autor=autor, comentario=comentario)
        mensaje = 'El comentario ha sido enviado correctamente.'
        tipo_msj = 'info'
    # Si no se ha ingresado un autor
    else:
        entrada.comentario_set.create(comentario=comentario)
        mensaje = 'El comentario ha sido enviado correctamente.'
        tipo_msj = 'info'
    return render(request, 'blog/pub.html', {'entrada': entrada, 'mensaje': mensaje, 'tipo_msj': tipo_msj}, context_instance=RequestContext(request))

