from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.
def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))
def iniciarsesion(request):
    return render_to_response('signin.html',context_instance=RequestContext(request))

def pensum(request):
    return render_to_response('pensum.html',context_instance=RequestContext(request))

def opcioncalificacion(request):
    return render_to_response('OpcionCalificaciones.html',context_instance=RequestContext(request))

def matricula(request):
    return render_to_response('matricula.html',context_instance=RequestContext(request))

def matriculamateria(request):
    return render_to_response('matricula_materia.html',context_instance=RequestContext(request))

def horario(request):
    return render_to_response('horario.html',context_instance=RequestContext(request))

def financiera(request):
    return render_to_response('matriculafinanciera.html',context_instance=RequestContext(request))