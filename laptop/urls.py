from django.conf.urls import url, include

from laptop.views import index, laptop_view, laptop_list, laptop_edit, laptop_delete, \
     LaptopList, LaptopCreate, LaptopUpdate, LaptopDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', LaptopCreate.as_view(), name='laptop_crear'),
    url(r'^listar$', LaptopList.as_view(), name='laptop_listar'),
    url(r'^editar/(?P<pk>\d+)/$', LaptopUpdate.as_view(), name='laptop_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', LaptopDelete.as_view(), name='laptop_eliminar'),
]


