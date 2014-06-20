from django.contrib import admin

from fileshower.models import Document


class DocumentAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'content', 'lastviewed',)
    
    
admin.site.register(Document, DocumentAdmin)
