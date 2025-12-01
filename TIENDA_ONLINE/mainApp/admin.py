from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Categoria, Producto, Insumo, PlataformaOrigen, Pedido


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio_base", "destacado")
    list_filter = ("categoria", "destacado")
    search_fields = ("nombre", "descripcion")
    list_editable = ("precio_base", "destacado")


@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "cantidad_disponible", "unidad", "marca", "color")
    list_filter = ("tipo", "marca", "color")
    search_fields = ("nombre", "marca", "color")


@admin.register(PlataformaOrigen)
class PlataformaOrigenAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cliente_nombre",
        "plataforma_origen",
        "estado",
        "estado_pago",
        "creado",
    )
    list_filter = ("estado", "estado_pago", "plataforma_origen")
    search_fields = ("cliente_nombre",)
