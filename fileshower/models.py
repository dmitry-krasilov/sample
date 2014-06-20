# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    name = models.FilePathField(verbose_name='Name')
    content = models.TextField(verbose_name='Content')
    lastviewed = models.DateTimeField(auto_now = True, verbose_name='Date viewed')
    
    def __unicode__(self):
        return self.name
        
