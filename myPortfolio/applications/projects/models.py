from django.db import models
#
from .managers import ProjectsManager

class Project(models.Model):

    FRAMEWORK_CHOICES = (
        ('django', 'Django'),
        ('springboot', 'Springboot'),
        ('nodejs', 'Node js'),
        ('laravel', 'Laravel')
    )

    project_name = models.CharField(
        verbose_name='Project name',
        max_length=200
    )
    project_link = models.URLField()
    url_enabled = models.BooleanField()
    disabled_link_msg = models.TextField(blank=True)
    project_git = models.URLField()
    cover_img = models.ImageField(upload_to='cover_imgs')
    description = models.TextField()
    framework = models.CharField(max_length=100, choices=FRAMEWORK_CHOICES)

    objects = ProjectsManager()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.project_name
