# -*- encoding: utf-8 -*-
from models import Estudiante

def info_estudiante(request):
	try:
		if request.user.is_authenticated:
			estudiante = Estudiante.objects.get(usuario=request.user)
			return {'estudiante':estudiante}
	except Estudiante.DoesNotExist:
		raise
	