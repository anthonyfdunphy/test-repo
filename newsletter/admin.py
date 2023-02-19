from django.contrib import admin
from .models import NewsletterSignup

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name','email')

admin.site.register(NewsletterSignup)
