from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import Producto, Categoria

# Create your views here.
def cliente(req):
    # Filtros
    categoria_id = req.GET.get("categoria")
    solo_destacados = req.GET.get("destacados")
    termino_busqueda = req.GET.get("q")

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    if solo_destacados:
        productos = productos.filter(destacado=True)

    # Buscador
    if termino_busqueda:
        productos = productos.filter(
            Q(nombre__icontains=termino_busqueda) |
            Q(descripcion__icontains=termino_busqueda)
        )

    contexto = {
        "productos": productos,
        "categorias": categorias,
        "categoria_seleccionada": categoria_id,
        "solo_destacados": bool(solo_destacados),
        "termino_busqueda": termino_busqueda or "",
    }
    return render(req, "cliente.html", contexto)

def producto_detalle(req, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    # Lista de imágenes
    imagenes = []
    if producto.imagen_1:
        imagenes.append(producto.imagen_1)
    if producto.imagen_2:
        imagenes.append(producto.imagen_2)
    if producto.imagen_3:
        imagenes.append(producto.imagen_3)

    contexto = {
        "producto": producto,
        "imagenes": imagenes,
    }
    return render(req, "producto_detalle.html", contexto)

def solicitar_producto(request, producto_id):
    # Vista temporal, luego aquí irá el formulario real (punto 9)
    return HttpResponse(
        f"Formulario de solicitud para el producto #{producto_id} (en construcción)."
    )