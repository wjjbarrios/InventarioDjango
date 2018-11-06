from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_productos, name ='lista_productos'),
    url(r'^producto/nueva/$', views.producto_nuevo, name='producto_nueva'),
    url(r'^producto/(?P<pk>[0-9]+)/detalle/$', views.detalle_producto, name='detalle_producto'),
    url(r'^producto/(?P<pk>[0-9]+)/eliminar/$', views.Eliminar_producto, name='eliminar_producto'),
    url(r'^producto/(?P<pk>[0-9]+)/editar/$', views.Editar_producto, name='editar_producto'),

    #urls marca_nueva
    url(r'^marca/lista/$', views.lista_marcas, name ='lista_marcas'),
    url(r'^marca/nueva/$', views.marca_nueva, name='marca_nueva'),
    url(r'^marca/(?P<pk>[0-9]+)/detalle/$', views.detalle_marca, name='detalle_marca'),
    url(r'^marca/(?P<pk>[0-9]+)/eliminar/$', views.Eliminar_marca, name='eliminar_marca'),
    url(r'^marca/(?P<pk>[0-9]+)/editar/$', views.Editar_marca, name='editar_marca'),

 #urls categoria
    url(r'^categoria/lista/$', views.lista_categoria, name ='lista_categoria'),
    url(r'^categoria/nueva/$', views.categoria_nueva, name='categoria_nueva'),
    url(r'^categoria/(?P<pk>[0-9]+)/detalle/$', views.detalle_categoria, name='detalle_categoria'),
    url(r'^categoria/(?P<pk>[0-9]+)/eliminar/$', views.Eliminar_categoria, name='eliminar_categoria'),
    url(r'^categoria/(?P<pk>[0-9]+)/editar/$', views.Editar_categoria, name='editar_categoria'),
    ]
