from django.db import models
from django.contrib.auth.models import User

class Section(models.Model): 
    title = models.CharField("Section Title", max_length=100)
    slug = models.SlugField("Section Slug", max_length=100)

    last_editted_by = models.ForeignKey(User)


