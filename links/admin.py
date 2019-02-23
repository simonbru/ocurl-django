from django.contrib import admin
from .models import Link

# Register your models here.
@admin.register(Link)
class LinkModelAdmin(admin.ModelAdmin):
    pass
