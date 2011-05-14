from hoopoid.inventory.models import Hoop
from django.contrib import admin

class HoopAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'title_color', 'quantity', 'price', 'image')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Hoop, HoopAdmin)
