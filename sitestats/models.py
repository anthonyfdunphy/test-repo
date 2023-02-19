from django.db import models
from django.utils import timezone

# This class is to track page views on the home page
class SiteStats(models.Model):
    url = models.CharField(max_length=200, unique=True)
    views = models.PositiveIntegerField(default=0)
    webpage = "Home Page"

    def __str__(self):
        return self.url

    class Meta:
        unique_together = ('url',)
        verbose_name = 'Homepage Views'
        verbose_name_plural = 'Homepage Views'
