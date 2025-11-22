from django.contrib import admin
from .models import neon

# Register your models here.
@admin.register(neon)
class NeonAdmin(admin.ModelAdmin):
    list_display = ('name', )
    