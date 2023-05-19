from django.shortcuts import render
from django.views.generic import ListView
#
from .models import Skill

class FrontEndSkillsView(ListView):

    template_name = 'skills/front_end.html'
    context_object_name = 'skills'

    def get_queryset(self):
        skills = Skill.objects.get_frontend_skills()
        return skills

class BackEndSkillsView(ListView):

    template_name = 'skills/back_end.html'
    context_object_name = 'skills'

    def get_queryset(self):
        skills = Skill.objects.get_backend_skills()
        return skills
