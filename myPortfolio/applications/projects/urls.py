from django.urls import path
#
from .views import (
    PythonProjectsView,
    JavaProjectsView,
    ExpressProjectView,
    ProjectDetails
)

app_name = 'projects_app'

urlpatterns = [
    path(
        'projects/spingboot',
        JavaProjectsView.as_view(),
        name='projects-java'
    ),
    path(
        'projects/django',
        PythonProjectsView.as_view(),
        name='projects-django'
    ),
    path(
        'projects/express',
        ExpressProjectView.as_view(),
        name='projects-express'
    ),
    path(
        'projects/detials/<projectId>',
        ProjectDetails.as_view(),
        name='project-details'
    ),
]


