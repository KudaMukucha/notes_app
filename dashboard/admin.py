from django.contrib import admin
from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display =('title','is_deleted','updated_at')
    search_fields =('title',)
admin.site.register(Note,NoteAdmin)