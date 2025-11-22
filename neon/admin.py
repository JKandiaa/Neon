from django.contrib import admin
from .models import Neon


# Register your models here.
@admin.register(Neon)
class NeonAdmin(admin.ModelAdmin):
    list_display = ('name', )
    