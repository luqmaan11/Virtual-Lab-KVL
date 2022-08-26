from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('explain', views.explain, name='explain'),
    path('code', views.code, name='code'),
    path('vlab', views.vlab, name='vlab'),
    path('components', views.components, name='components'),
    path('simpe', views.simple, name='simple'),
    path('series', views.series, name='simple'),
    path('seriescircuit', views.seriescircuit, name='simple'),
    path('parallel', views.parallel, name='parallel'),
    path('parallelcircuit', views.parallelcircuit, name='parallelcircuit'),
    path('sparallel', views.sparallel, name='sparallel'),
    path('sparallelcircuit', views.sparallelcircuit, name='sparallelcircuit'),
]
