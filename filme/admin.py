from django.contrib import admin
from .models import Filme, Episodio  # Filme é a classe

# Register your models here.

admin.site.register(Filme)
admin.site.register(Episodio)

