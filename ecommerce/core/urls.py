from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda req: redirect('/produtos/'), name="home"),
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('clientes/', include('clientes.urls'))
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, 
                    document_root=settings.MEDIA_ROOT)
