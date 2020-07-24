from django.contrib import admin
from .models import Cryptid, Location

class CryptidAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['discovery_date']}),
    ]


admin.site.register(Cryptid)
admin.site.register(Location)
# Register your models here.
