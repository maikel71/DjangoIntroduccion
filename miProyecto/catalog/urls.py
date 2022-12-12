# Agregamos
from django.conf.urls import url
from . import views

urlpatterns = [
    # r'^$' --> es una exprecion irregular,
    # esto quiere decir cuando la peticion sea barra,
    # esto significa que empieza y termina por nada,
    # cuando la peticion sea nada va a tener que disparar
    # la funcion index del modulo views(views.index)
    # y se va a llamar index(name='index')
    url(r'^$', views.index, name='index')
]
