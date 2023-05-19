from django.db import models

class SkillsManager(models.Manager):

    def get_frontend_skills(self):
        return self.filter(belongs_to='F').order_by('-id')
    
    def get_backend_skills(self):
        return self.filter(belongs_to='B').order_by('-id')