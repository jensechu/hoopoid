from hoopoid.content.models import Section
from django.contrib import admin

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'last_editted_by')

    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        obj.last_editted_by = request.user
        obj.save()

admin.site.register(Section, SectionAdmin)
