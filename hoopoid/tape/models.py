from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    __str__ = __unicode__

class Tape(models.Model):
    tape_type = models.ForeignKey(Type)
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()
