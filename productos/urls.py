from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_productos, name ='lista_productos'),
    url(r'^producto/nueva/$', views.producto_nuevo, name='producto_nueva'),
    url(r'^producto/(?P<pk>[0-9]+)/detalle/$', views.detalle_producto, name='detalle_producto'),
    url(r'^producto/(?P<pk>[0-9]+)/eliminar/$', views.Eliminar_producto, name='eliminar_producto'),
    url(r'^producto/(?P<pk>[0-9]+)/editar/$', views.Editar_producto, name='editar_producto'),
    ]
