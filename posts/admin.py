from django.contrib import admin
from .models import Categoria, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Categoria)