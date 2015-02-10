from django.db import models
from slugify import slugify
from urlparse import urljoin
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    site = models.URLField(blank=True, null=True)
    rate = models.IntegerField(default=50)
    bank = models.CharField(max_length=100, default='anz')
    bank_account_name = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def get_logo(self):
        return urljoin(settings.STATIC_URL, 'img/logo/' + self.slug + '.jpg')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)
