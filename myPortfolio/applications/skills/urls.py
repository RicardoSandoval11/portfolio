from django.urls import path
#
from .views import FrontEndSkillsView, BackEndSkillsView

app_name = 'skills'

urlpatterns = [
    path(
        'skills-front-end/',
        FrontEndSkillsView.as_view(),
        name='front-end'
    ),
    path(
        'skills-back-end/',
        BackEndSkillsView.as_view(),
        name='back-end'
    )
]