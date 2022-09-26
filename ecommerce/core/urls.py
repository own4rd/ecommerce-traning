from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda req: redirect('/produtos/'), name="home"),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('clientes/', include('clientes.urls'))
]
