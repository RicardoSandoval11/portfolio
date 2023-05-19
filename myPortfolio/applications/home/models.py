from django.db import models

class Home(models.Model):

    name = models.CharField(verbose_name='name', max_length=100)
    role = models.CharField(verbose_name='role', max_length=200)
    profile_img = models.ImageField(verbose_name='Image', upload_to='home')
    presentation = models.TextField()
    selected = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'
    
    def __str__(self):
        return self.name

class About(models.Model):

    univeristy = models.TextField()
    univeristy_img = models.ImageField(upload_to='about')
    laboral_experience = models.TextField()
    laboral_experience_img = models.ImageField(upload_to='about')
    selected = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
    
    def __str__(self):
        return str(self.id)

class Certificates(models.Model):

    image = models.ImageField(upload_to='certificates')
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
    
    def __str__(self):
        return str(self.id)+' - '+self.title


