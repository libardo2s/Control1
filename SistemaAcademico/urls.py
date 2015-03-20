from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'SistemaAcademico.views.index', name='home'),
    url(r'^login/', 'SistemaAcademico.views.iniciarsesion', name='home'),
     url(r'^pensum/', 'SistemaAcademico.views.pensum', name='pensum'),
     url(r'^opcion/', 'SistemaAcademico.views.opcioncalificacion', name='opcion'),
     url(r'^matricula/', 'SistemaAcademico.views.matricula', name='opcion'),
     url(r'^matriculamateria/', 'SistemaAcademico.views.matriculamateria', name='opcion'),
    url(r'^horario/', 'SistemaAcademico.views.horario', name='opcion'),
    url(r'^financiera/', 'SistemaAcademico.views.financiera', name='opcion'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
