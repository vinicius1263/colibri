from django.contrib import admin

# Register your models here.
from .models import Produto, Produtolancado, Mesa

admin.site.register(Produto)
admin.site.register(Produtolancado)
admin.site.register(Mesa)
