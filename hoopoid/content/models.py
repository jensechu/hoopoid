from django.db import models
from django.contrib.auth.models import User

class Section(models.Model): 
    title = models.CharField("Section Title", max_length=100)
    slug = models.SlugField("Section Slug", max_length=100, unique=True)    

    last_editted_by = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title
    __str__ = __unicode__

    def __repr__(self):
        return u"<Section(%s): %s>" % (self.pk, unicode(self))

class SectionContent(models.Model):
    section = models.ForeignKey(Section)

    title = models.CharField("Header Title", max_length=100)
    slug = models.SlugField("Content Slug", max_length=100, unique=True)
    css_class = models.CharField("CSS Class", max_length=50)
    image = models.ImageField("Section Image", upload_to="section_images", blank=True)
    text = models.TextField("Section Text", blank=True)
    
    last_editted_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.title
    __str__ = __unicode__

    def __repr__(self):
        return u"<Section Content(%s, %s): %s>" % (string(self.section), self.pk, unicode(self))
