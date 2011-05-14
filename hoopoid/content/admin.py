from hoopoid.content.models import Section, SectionContent
from django.contrib import admin

class LastEdittedByAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.last_editted_by = request.user
        obj.save()
    

class SectionAdmin(LastEdittedByAdmin):
    list_display = ('title', 'default', 'last_editted_by')
    fieldsets = (
        (None, {'fields': ('title', 'slug', 'default')}),
    )
    prepopulated_fields = {"slug": ("title",)}
    
class SectionContentAdmin(LastEdittedByAdmin):
    list_display = ('title', 'section', 'last_editted_by')
    fieldsets = (
        (None, {'fields': ('section', 'title', 'slug', 'css_class', 'image', 'text')}),
    )

    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Section, SectionAdmin)
admin.site.register(SectionContent, SectionContentAdmin)
