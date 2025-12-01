from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("producto/<int:producto_id>/", views.producto_detalle, name="producto_detalle"),
    path("producto/<int:producto_id>/solicitar/", views.solicitar_producto, name="solicitar_producto"),
    path('', views.cliente, name="cliente"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

