# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    name = models.FilePathField('Name')
    content = models.TextField('Content')
    lastviewed = models.DateTimeField('Date viewed', auto_now=True)
    
    def __unicode__(self):
        return self.name
        
