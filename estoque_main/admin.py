from django.contrib import admin

from estoque_main.models.categoria import Categoria
from estoque_main.models.produto import Produto
from estoque_main.models.usuario import Usuario
from estoque_main.models.administrador import Administrador
from estoque_main.models.historico import Historico


admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Historico)
