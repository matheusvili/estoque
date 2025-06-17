from django.contrib import admin

from estoque_main.models.categoria import Categoria
from estoque_main.models.produto import Produto
from usuario.models import Usuario
from estoque_main.models.administrador import Administrador
from estoque_main.models.retirada import Retirada

@admin.register(Retirada)
class RetiradaAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "status")
    ordering =("-id",)
    list_per_page= 25

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Administrador)


