"""apirest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from consumo.views import guesaf,guesas,laden,content,contenido,agregar_ingrediente,nada
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamburguesa',guesaf),
    path('hamburguesa/<int:idef>', guesas),
    path('hamburguesa/<str:idef>',laden),
    path('ingrediente',content),
    path('ingrediente/<int:idif>',contenido),
    path('hamburguesa/<int:bur>/ingrediente/<int:ing>',agregar_ingrediente),
    path('ingrediente/<str:idef>',laden),
    path('hamburguesa/<str:bur>/ingrediente/<int:ing>', nada),
    path('hamburguesa/<str:bur>/ingrediente/<str:ing>', nada),
    path('hamburguesa/<int:bur>/ingrediente/<str:ing>', nada),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
