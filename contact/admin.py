from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'message')

admin.site.register(Contact, ContactAdmin)
