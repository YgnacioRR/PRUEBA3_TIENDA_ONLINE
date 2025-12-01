from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "cliente_nombre",
            "cliente_email",
            "cliente_telefono",
            "cliente_red_social",
            "descripcion",
            "fecha_solicitada",
            "imagen_referencia_1",
            "imagen_referencia_2",
            "imagen_referencia_3",
        ]
        widgets = {
            "cliente_nombre": forms.TextInput(attrs={"class": "form-control"}),
            "cliente_email": forms.EmailInput(attrs={"class": "form-control"}),
            "cliente_telefono": forms.TextInput(attrs={"class": "form-control"}),
            "cliente_red_social": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "fecha_solicitada": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "imagen_referencia_1": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "imagen_referencia_2": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "imagen_referencia_3": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
        labels = {
            "cliente_nombre": "Nombre del cliente",
            "cliente_email": "Email",
            "cliente_telefono": "Teléfono",
            "cliente_red_social": "Red social",
            "descripcion": "Descripción de lo solicitado",
            "fecha_solicitada": "Fecha en que necesita el producto (opcional)",
            "imagen_referencia_1": "Imagen de referencia 1",
            "imagen_referencia_2": "Imagen de referencia 2",
            "imagen_referencia_3": "Imagen de referencia 3",
        }
