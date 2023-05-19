from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
#
from .models import Home, About, Certificates

class HomeView(TemplateView):

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        context ['data'] = Home.objects.get(selected=True)

        return context

class AboutView(View):

    template_name = 'about/about_me.html'

    def get(self, request, *args, **kwargs):

        data = About.objects.get(selected=True)

        certificates = Certificates.objects.all()

        return render(request, self.template_name, 
                    {
                        'data': data,
                        'certificates': certificates
                    })


