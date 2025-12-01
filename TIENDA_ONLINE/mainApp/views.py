from django.shortcuts import render
from django.db.models import Q
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