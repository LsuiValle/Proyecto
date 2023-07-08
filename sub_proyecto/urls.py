from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('index',views.index, name='index'),
    path('paginas/editar',views.editarp, name='editarp'),
    path('paginas/crear',views.crearp, name='crearp'),
    path('paginas/eliminar/<int:id>',views.eliminarp, name='eliminarp'),
    path('paginas/editar/<int:id>',views.editarp, name='editarp'),
    path('paginas/agregar',views.agregarp, name='agregarp'),
    path('usuarios/editar',views.editaru, name='editaru'),
    path('usuarios/crear',views.crearu, name='crearu'),
    path('usuarios/listar',views.listar, name='listar'),
    path('usuarios/agregar',views.agregaru, name='agregaru'),
    path('usuarios/eliminar/<int:id>',views.eliminaru, name='eliminaru'),
    path('usuarios/editar/<int:id>',views.editaru, name='editaru'),
    path('buscar/', views.buscar, name='buscar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)