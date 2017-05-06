from django.conf.urls import url, include

from laptop.views import index

urlpatterns = [
    url(r'^$', index),
]
