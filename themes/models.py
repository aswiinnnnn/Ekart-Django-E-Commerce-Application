from django.db import models

# Models for themes


class SiteSettings(models.Model):
    banner = models.ImageField(upload_to='media/site/', null=True, blank=True)
    captions =  models.TextField(null=True, blank=True)
    