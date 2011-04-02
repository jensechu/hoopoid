from django.db import models

class Hoop(models.Model):
    hoop = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='hoops')
    
    HEADER_COLORS = (
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('green', 'Green'),
        ('yellow', 'Yellow')
        )
    header = models.CharField(max_length=10, choices=HEADER_COLORS)
