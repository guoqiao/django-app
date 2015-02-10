from django.db import models
from slugify import slugify
from urlparse import urljoin
from django.conf import settings
from os.path import abspath, dirname
from path import path
APP_ROOT = path(dirname(abspath(__file__)))
APP_NAME = APP_ROOT.name

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
        return urljoin(settings.STATIC_URL, '%s/logo/%s.jpg' % (APP_NAME, self.slug))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)
