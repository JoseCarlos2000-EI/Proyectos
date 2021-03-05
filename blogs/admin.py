from django.contrib import admin
from .models import persona,Conocimiento,Proyecto
# Register your models here.
admin.site.register(persona)
admin.site.register(Conocimiento)
admin.site.register(Proyecto)