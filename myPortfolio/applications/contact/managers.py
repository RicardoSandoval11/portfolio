from django.db import models

class ContactManger(models.Manager):

    def get_last_contact(self):
        return self.all().order_by('id').first()