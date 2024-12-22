from django.contrib import admin
from .models import Livro, Autor, Genero, Observacoes, Video

# Register your models here.

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Video)
admin.site.register(Observacoes)