from django.db import models

class ProjectsManager(models.Manager):

    def get_technology_projects(self, technology):
        return self.filter(
            framework=technology
        )