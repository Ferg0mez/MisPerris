from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index,name="inicio"),
    url(r'^Usuarios/$',views.gestionarUsuarios,name="gestionarUsuarios"),
    url(r'^registro/$',views.registro,name="registro"),
    url(r'^Mascota/$',views.MascotaCreate.as_view(),name="MascotaNueva"),
    url(r'^MascotaLista',views.MascotaList.as_view(),name="listaMascota"),
    url(r'^Editar/(?P<pk>\d+)/$',views.MascotaUpdate.as_view(),name="editarMascota"),
    url(r'^Eliminar/(?P<pk>\d+)/$',views.MascotaDelete.as_view(),name="eliminarMascota"),
    url(r'^login/$',views.ingresar,name="login"),
    url(r'^salir/$',views.salir,name="logout")

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Para poder hacer que la foto cargue en la pagina.