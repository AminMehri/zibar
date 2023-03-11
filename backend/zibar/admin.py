from django.contrib import admin
from .models import ContactUs

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'seen')
    search_fields = ['full_name', 'subject', 'content']

admin.site.register(ContactUs, ContactUsAdmin)
