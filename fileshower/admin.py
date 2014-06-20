# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from fileshower.models import Document


class FileTypeListFilter(admin.SimpleListFilter):
    title = 'File type'
    parameter_name = 'type'
    
    def lookups(self, request, model_admin):
        return (
            ('py', '.py files'),
            ('txt', '.txt files'),
            ('other', 'Other files'),
        )
        
    def queryset(self, request, queryset):
        if self.value() == 'py':
            tmp_id_queryset = [x.id for x in queryset if x.name.split(".")[-1] == 'py']
            return queryset.filter(pk__in=tmp_id_queryset)
            
        if self.value() == 'txt':
            tmp_id_queryset = [
                x.id for x in queryset
                if x.name.split(".")[-1] == 'txt'
            ]
            return queryset.filter(pk__in=tmp_id_queryset)
            
        if self.value() == 'other':
            special = ('py','txt')
            tmp_id_queryset = [
                x.id for x in queryset 
                if x.name.split(".")[-1] not in special
            ]
            return queryset.filter(pk__in=tmp_id_queryset)
            

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
    list_filter = ('name','lastviewed', FileTypeListFilter,)
    form = DocumentAdminForm


admin.site.register(Document, DocumentAdmin)
