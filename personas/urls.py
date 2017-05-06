from django.conf.urls import url, include

from personas.views import index

urlpatterns = [
    url(r'^$', index),
]