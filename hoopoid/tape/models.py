from django.db import models


class Type(models.Model):
    TAPE_TYPES = (
        ('grip', 'Grip'),
        ('base', 'Base'),
        ('accent', 'Accent')
        )
    tape_type = models.CharField(max_length=10, choices=TAPE_TYPES)

class Tape(models.Model):
    tape_type = models.ForeignKey(Type)
    color = models.CharField(max_length=100)
    quantity = models.IntegerField()
    
