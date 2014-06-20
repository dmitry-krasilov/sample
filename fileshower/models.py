from django.db import models


class Document(models.Model):
    name = models.FilePathField(verbose_name='Name')
    content = models.TextField(verbose_name='Content')
    lastviewed = models.DateTimeField(verbose_name='Date viewed')
    
    def __unicode__(self):
        return self.name
        
