from hoopoid.tape.models import Type, Tape
from django.contrib import admin

class TapeAdmin(admin.ModelAdmin):
    list_display = ('tape_type', 'color', 'quantity')

admin.site.register(Type)
admin.site.register(Tape, TapeAdmin)
