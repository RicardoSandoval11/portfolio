from django.db import models
#
from .managers import ContactManger

class Contact(models.Model):

    linkedin = models.URLField(blank=True)
    gmail = models.EmailField(blank=True)
    whatsapp_link = models.URLField(max_length=30, blank=True)
    my_number = models.TextField(max_length=50, blank=True)

    objects = ContactManger()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return str(self.id)
