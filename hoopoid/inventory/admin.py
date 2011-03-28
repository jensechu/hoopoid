from hoopoid.inventory.models import Hoop
from django.contrib import admin

class HoopAdmin(admin.ModelAdmin):
    list_display = ('hoop', 'quantity', 'price', 'image')

admin.site.register(Hoop, HoopAdmin)
