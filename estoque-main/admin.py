from django.contrib import admin

from estoque.models.categoria import Categoria
from estoque.models.produto import Produto
from estoque.models.usuario import Usuario
from estoque.models.administrador import Administrador
from estoque.models.historico import Historico


admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Historico)
