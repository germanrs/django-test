from django.conf.urls import url, include

from laptop.views import index, laptop_view, laptop_list, laptop_edit, laptop_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', laptop_view, name='laptop_crear'),
    url(r'^listar$', laptop_list, name='laptop_listar'),
    url(r'^editar/(?P<laptop_id>\d+)/$', laptop_edit, name='laptop_editar'),
    url(r'^eliminar/(?P<laptop_id>\d+)/$', laptop_delete, name='laptop_eliminar'),
]


