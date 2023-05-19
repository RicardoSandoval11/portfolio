from django.db import models
#
from applications.projects.models import Project
from .managers import DescriptionManager

class DescriptionProject(models.Model):

    view_project_title = models.CharField(
        max_length=200,
        verbose_name='View project name'
    )
    view_project_description = models.TextField()
    view_project_img = models.ImageField(upload_to='desc_imgs')
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    objects = DescriptionManager()

    class Meta:
        verbose_name = 'Description'
        verbose_name_plural = 'Description'
    
    def __str__(self):
        return self.project.project_name +' - '+self.view_project_title
    



