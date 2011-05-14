from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Section(models.Model): 
    title = models.CharField("Section Title", max_length=100)
    slug = models.SlugField("Section Slug", max_length=100, unique=True)    
    default = models.BooleanField("Default Section?", default=False)

    last_editted_by = models.ForeignKey(User)

    def clean(self):
        print "Model clean method called"
        if Section.objects.count() == 0:
            self.default = True
        else:
            print "This instance is not the first Section model."
            
        if self.default:
            Section.objects.all().update(default=False)
        else: 
            if not Section.objects.filter(default=True).exclude(pk=self.pk).count():
                raise ValidationError('You must have a default Section.')

    def save(self, *args, **kwargs):
        self.clean()
        return super(Section, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
    __str__ = __unicode__

    def __repr__(self):
        return u"<Section(%s): %s>" % (self.pk, unicode(self))

class SectionContent(models.Model):
    section = models.ForeignKey(Section, related_name="contents")

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
        return u"<Section Content(%s, %s): %s>" % (str(self.section), self.pk, unicode(self))

@receiver(pre_delete, sender=Section, dispatch_uid="Validating the Section model.")
def default_delete_check(sender, instance, **kwargs):
    if not sender.objects.filter(default=True).exclude(pk=instance.pk).count():
        try:
            new_default = sender.objects.filter(default=False).latest("pk")
            new_default.default = True
            new_default.save()
            print "Promoted to default:", new_default
        except sender.DoesNotExist:
            print "No Sections to promote to default."
        print "Deleting only default:", instance
    else:
        print "There is another valid default specified."
