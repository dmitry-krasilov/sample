# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django import forms
from fileshower.models import Document

class FileTypeListFilter(admin.SimpleListFilter):
    title = _('Type of file')

    parameter_name = 'type'
    
"""
    def lookups(self, request, model_admin):
        
        return (
            ('py', _('.py files')),
            ('txt', _('.txt files')),
            ('other', _('other files'),
        )
"""    

class DocumentAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DocumentAdminForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['content'].widget.attrs['readonly'] = True
            self.fields['content'].widget.attrs['cols'] = 72
            self.fields['content'].widget.attrs['rows'] = 30
            
    content = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = Document


class DocumentAdmin(admin.ModelAdmin):
    fields = ('content', 'name', 'lastviewed',)
    list_display = ('name', 'lastviewed',)
    readonly_fields = ('name', 'lastviewed',)
    list_filter = ('name','lastviewed')
    form = DocumentAdminForm


admin.site.register(Document, DocumentAdmin)
