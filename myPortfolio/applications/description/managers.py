from django.db import models


class DescriptionManager(models.Manager):

    def get_description_by_project(self, project_id):
        return self.filter(
            project=project_id
        ).order_by('id')