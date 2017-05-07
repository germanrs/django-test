from django.conf.urls import url, include

from laptop.views import index, laptop_view, laptop_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^/nuevo$', laptop_view, name='laptop_crear'),
    url(r'^/listar$', laptop_list, name='laptop_listar'),
]

