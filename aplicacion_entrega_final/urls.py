from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio,name='inicio'),

    #peliculas

    path('peliculas/',listapeliculas.as_view(),name='peliculas'),
    path('añadirpelicula/',añadirpelicula.as_view(),name='añadirpelicula'),
    path('detallespelicula/<int:pk>/',detallespeliculas.as_view(),name='detallespelicula'),
    path('eliminarpelicula/<int:pk>/',eliminarpelicula.as_view(),name='eliminarpelicula'),
    path('editarpelicula/<int:pk>/',editararpelicula.as_view(),name='editarpelicula'),

    #series

    path('series/',listaseries.as_view(),name='series'),
    path('añadirserie/',añadirserie.as_view(),name='añadirserie'),
    path('detallesserie/<int:pk>/',detallesserie.as_view(),name='detallesserie'),
    path('eliminarserie/<int:pk>/',eliminarserie.as_view(),name='eliminarserie'),
    path('editarserie/<int:pk>/',editarserie.as_view(),name='editarserie'),

    #programas

    path('programas/',listaprogramas.as_view(),name='programas'),
    path('añadirprograma/',añadirprograma.as_view(),name='añadirprograma'),
    path('detallesprograma/<int:pk>/',detallesprograma.as_view(),name='detallesprograma'),
    path('eliminarprograma/<int:pk>/',eliminarprograma.as_view(),name='eliminarprograma'),
    path('editarprograma/<int:pk>/',editarprograma.as_view(),name='editarprograma'),

    #documentales

    path('documentales/',listadocumental.as_view(),name='documentales'),
    path('añadirdocumental/',añadirdocumental.as_view(),name='añadirdocumental'),
    path('detallesdocumental/<int:pk>/',detallesdocumental.as_view(),name='detallesdocumental'),
    path('eliminardocumental/<int:pk>/',eliminardocumental.as_view(),name='eliminardocumental'),
    path('editardocumental/<int:pk>/',editardocumental.as_view(),name='editardocumental'),

    #login,logout y registro

    path('logearse/',logearse,name='logearse'),
    path('registrarse/',registrarse,name='registrarse'),
    path('deslogeo/',LogoutView.as_view(template_name='deslogeo.html'),name='deslogeo'),
    path('editarusuario/',editarusuario,name='editarusuario'),

    #Asignacion de avatar
    path('asignaravatar/',asignaravatar,name='asignaravatar'),

    #acerca de mi
    path('acercademi/',acercademi,name='acercademi'),

]