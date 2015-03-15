from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'SistemaAcademico.views.index', name='home'),
    url(r'^login/', 'SistemaAcademico.views.IniciarSesion', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
