from django.db import models
import uuid
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos"
    )
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    # Hasta 3 imágenes asociadas al producto
    imagen_1 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen_2 = models.ImageField(upload_to="productos/", blank=True, null=True)
    imagen_3 = models.ImageField(upload_to="productos/", blank=True, null=True)
    destacado = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre


class Insumo(models.Model):
    nombre = models.CharField(max_length=150)
    tipo = models.CharField(max_length=100)
    cantidad_disponible = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=30, blank=True, help_text="Ej: unidades, kg, metros…")
    marca = models.CharField(max_length=100, blank=True)
    color = models.CharField(max_length=50, blank=True)
    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"
        ordering = ["tipo", "nombre"]
    def __str__(self):
        return self.nombre


class PlataformaOrigen(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ["nombre"]
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ("SOLICITADO", "Solicitado"),
        ("APROBADO", "Aprobado"),
        ("EN_PROCESO", "En proceso"),
        ("REALIZADA", "Realizada"),
        ("ENTREGADA", "Entregada"),
        ("FINALIZADA", "Finalizada"),
        ("CANCELADA", "Cancelada"),
    ]
    ESTADOS_PAGO = [
        ("PENDIENTE", "Pendiente"),
        ("PARCIAL", "Parcial"),
        ("PAGADO", "Pagado"),
    ]

    cliente_nombre = models.CharField(max_length=150)
    cliente_email = models.EmailField(blank=True)
    cliente_telefono = models.CharField(max_length=30, blank=True)
    cliente_red_social = models.CharField(max_length=100, blank=True, help_text="Usuario o enlace de red social")
    producto_referencia = models.ForeignKey("Producto", on_delete=models.SET_NULL, null=True, blank=True, related_name="pedidos")
    descripcion = models.TextField()
    plataforma_origen = models.ForeignKey(PlataformaOrigen, on_delete=models.PROTECT, related_name="pedidos")
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default="SOLICITADO")
    estado_pago = models.CharField(max_length=20, choices=ESTADOS_PAGO, default="PENDIENTE")
    imagen_referencia_1 = models.ImageField(upload_to="referencias/", blank=True, null=True)
    imagen_referencia_2 = models.ImageField(upload_to="referencias/", blank=True, null=True)
    imagen_referencia_3 = models.ImageField(upload_to="referencias/", blank=True, null=True)
    fecha_solicitada = models.DateField(null=True, blank=True)
    token_seguimiento = models.CharField(max_length=50, unique=True, blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creado"]

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente_nombre}"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.estado == "FINALIZADA" and self.estado_pago != "PAGADO":
            raise ValidationError(
                "No se puede marcar el pedido como FINALIZADA si el pago no está PAGADO."
            )

    def save(self, *args, **kwargs):
        if not self.token_seguimiento:
            self.token_seguimiento = uuid.uuid4().hex
        super().save(*args, **kwargs)
