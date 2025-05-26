from django.contrib import admin

from .models import Categoria, Produto, Usuario, Adiministrador, Historico

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Usuario)
admin.site.register(Adiministrador)
admin.site.register(Historico)
