from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
#
from .models import Project
from applications.description.models import DescriptionProject

class JavaProjectsView(View):

    template_name = 'projects/java_projects.html'

    def get(self, request, *args, **kwargs):

        projects = Project.objects.get_technology_projects('springboot')

        return render(request, self.template_name, {'projects': projects})

class PythonProjectsView(View):

    template_name = 'projects/python_projects.html'

    def get(self, request, *args, **kwargs):

        projects = Project.objects.get_technology_projects('django')

        paginator = Paginator(projects, 2)
        page = self.request.GET.get('page')

        obj_page = paginator.get_page(page)

        return render(request, self.template_name, {
            'projects': obj_page,
            'paginator':paginator
        })

class ExpressProjectView(View):

    template_name = 'projects/nodejs_projects.html'

    def get(self, request, *args, **kwargs):

        projects = Project.objects.get_technology_projects('nodejs')

        return render(request, self.template_name, {'projects': projects})

class ProjectDetails(View):

    template_name = 'projects/project_details.html'

    def get(self, request, *args, **kwargs):

        projectId = self.kwargs['projectId']

        # try to find the project
        project = Project.objects.filter(id=projectId).first()

        if project is None:
            return render(request, 'generic/not_found.html')
        
        project_views = DescriptionProject.objects.filter(
            project=project
        )

        paginator = Paginator(project_views, 4)
        page = self.request.GET.get('page')

        obj_pag = paginator.get_page(page)

        return render(request, self.template_name, {
            'details':obj_pag,
            'paginator':paginator,
            'project_name':project.project_name
        })
