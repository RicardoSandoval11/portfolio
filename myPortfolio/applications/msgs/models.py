from django.db import models

class Msg(models.Model):

    message = models.TextField()
    contact_information = models.EmailField()

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
    
    def __str__(self):
        return str(self.id)+' - '+self.message
