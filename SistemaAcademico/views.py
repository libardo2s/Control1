from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from SistemaAcademico.forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

def iniciarsesion(request):

    if request.method == 'POST':

        formulario=FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data["usuario"]
            contrasena=formulario.cleaned_data["contrasena"]
        return HttpResponseRedirect('/')
    else:

         formulario=FormularioLogin()
    return render(request, 'signin.html', {'form': formulario})

def pensum(request):
    return render_to_response('pensum.html',context_instance=RequestContext(request))

def opcioncalificacion(request):
    return render_to_response('OpcionCalificaciones.html',context_instance=RequestContext(request))

def matricula(request):
    return render_to_response('matricula.html',context_instance=RequestContext(request))

def matriculamateria(request):
    m=Materia.objects.all()
    return render_to_response('matricula_materia.html',locals(),context_instance=RequestContext(request))

def horario(request):
    return render_to_response('horario.html',context_instance=RequestContext(request))

def financiera(request):
    return render_to_response('matriculafinanciera.html',context_instance=RequestContext(request))