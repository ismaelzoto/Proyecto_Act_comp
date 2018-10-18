from django.conf.urls import url
from apps.crud_alumnos.views import alumnosCreate, alumnosList, alumnosDelete, alumnosUpdate, alumnoShow, search, \
    estadoCreate,estadoDelete,estadoList,estadoShow,estadoUpdate, search_c

urlpatterns = [
    url(r'^nuevos/', alumnosCreate.as_view(), name='alumno_crear'),
    url(r'^listar/', alumnosList.as_view(), name='alumnos_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', alumnosDelete.as_view(), name='alumno_eliminar'),
    url(r'^modificar/(?P<pk>\d+)/$', alumnosUpdate.as_view(), name='alumno_editar'),
    url(r'^mostrar/(?P<pk>\d+)/$', alumnoShow.as_view(), name='alumno_mostrar'),
    url(r'^buscar/$', search, name='alumno_buscar'),
    #aqui inician las urls de estado
    url(r'^nuevo/', estadoCreate.as_view(), name='estado_crea'),
    url(r'^listo/', estadoList.as_view(), name='estado_lista'),
    url(r'^edita/(?P<pk>\d+)/$', estadoUpdate.as_view(), name='estado_edita'),
    url(r'^borrar/(?P<pk>\d+)/$', estadoDelete.as_view(), name='estado_borrar'),
    url(r'^ver/(?P<pk>\d+)/$', estadoShow.as_view(), name='estado_ver'),
    url(r'^busca/$', search_c, name='estado_busca')
]