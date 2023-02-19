from django.db import models
from django.utils import timezone

class NewsletterSignup(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    subscribed = models.BooleanField(default=True)
    date_subscribed = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Newsletter Signup'
        verbose_name_plural = 'Newsletter Signups'

    def __str__(self):
        return self.email
