from __future__ import unicode_literals

from django.contrib import admin
from .models import Producto, ProductoBase


class ProductoInLine(admin.StackedInline):
    model = Producto
    extra = 0

@admin.register(ProductoBase)
class ProductoBaseAdmin(admin.ModelAdmin):
    list_display = ('nombre','valor', 'valor_cantidad','factor', 'opciones_cobro', 'fecha','modificado')

