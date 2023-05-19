from django.db import models
#
from .managers import SkillsManager

class Skill(models.Model):

    BELONGS_TO_OPTIONS = (
        ('F', 'Front end'),
        ('B', 'Back end')
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_img = models.ImageField(upload_to='icons')
    belongs_to = models.CharField(choices=BELONGS_TO_OPTIONS, max_length=1)

    objects = SkillsManager()

    class Meta: 
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.name
