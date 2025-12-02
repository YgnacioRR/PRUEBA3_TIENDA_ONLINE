# Tienda de Artículos Personalizados - Django

Proyecto desarrollado como sistema web para una tienda dedicada a la elaboración de artículos personalizados
(poleras, polerones, tazones y productos 3D). Permite gestionar un catálogo público de productos, registrar pedidos
personalizados y administrar el flujo de trabajo desde el panel de administración de Django.

## Tecnologías utilizadas

- Python 3.12
- Django 5.2.8
- Bootstrap 5 (para el frontend)
- SQLite (base de datos por defecto)
- Pillow (para manejo de imágenes)

---

## Requerimientos

- Python 3.12 instalado
- pip instalado

Opcional pero recomendado: entorno virtual (`venv`).

---

## Instalación

``bash
# 1. Clonar el repositorio
git clone https://github.com/YgnacioRR/PRUEBA3_TIENDA_ONLINE.git
cd PRUEBA3_TIENDA_ONLINE/TIENDA_ONLINE

# 2. (Opcional) Crear y activar entorno virtual
python -m venv venv
venv\Scripts\activate  # En Windows

# 3. Instalar dependencias
pip install -r requirements.txt

---

##Configuracion inicial

Aplicar migraciones y crear un superusuario para el panel de administración:

python manage.py migrate
python manage.py createsuperuser

```Sigue las instrucciones en consola para crear el usuario administrador.```

Ejecutar el servidor de desarrollo
python manage.py runserver


Luego abrir en el navegador:

Catálogo público (vista cliente):
http://127.0.0.1:8000/

Panel de administración (Django Admin):
http://127.0.0.1:8000/admin/

---

## Funcionalidades principales

Administración interna (Django Admin)

Gestión de Categorías de productos.

Gestión de Productos (nombre, descripción, categoría, precio base, hasta 3 imágenes, destacado).

Gestión de Insumos (nombre, tipo, cantidad disponible, unidad, marca, color).

Gestión de Pedidos internos:

Estados del pedido: Solicitado, Aprobado, En proceso, Realizada, Entregada, Finalizada, Cancelada.

Control de estado de pago: Pendiente, Parcial, Pagado.

Imágenes de referencia del cliente.

Plataforma de origen del pedido (Facebook, Instagram, WhatsApp, Presencial, Página web, etc.).

Regla: no se puede marcar como FINALIZADA si el pago no está PAGADO.

Vista pública (cliente)

Catálogo de productos:

Listado con imagen, nombre, precio base.

Filtros por categorías.

Buscador de productos.

Marcado de productos destacados.

Detalle de producto:

Muestra descripción, precio, imágenes y botón "Solicitar este producto".

Formulario de solicitud de pedido:

Nombre del cliente, email, teléfono/red social.

Producto de referencia (si viene desde el catálogo).

Carga de imágenes de referencia.

Descripción de lo solicitado.

Fecha en que necesita el producto (opcional).

La plataforma se registra automáticamente como "Página web".

Seguimiento de pedido:

URL única basada en un token de seguimiento.

Muestra estado actual del pedido, estado de pago, imágenes de referencia, fecha solicitada y datos básicos.

---

Notas

Los archivos subidos por los clientes (imágenes) se almacenan en la carpeta media/, que no se incluye en el repositorio.

El sistema está pensado para uso local en entorno de desarrollo.

---
