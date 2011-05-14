from django.db import models

class Hoop(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField("Inventory Slug", max_length=100, unique=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='hoops')
    css_class = models.CharField("CSS Class", max_length=50)
    
    TITLE_COLORS = (
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('green', 'Green'),
        ('yellow', 'Yellow')
        )
    title_color = models.CharField(max_length=10, choices=TITLE_COLORS)
