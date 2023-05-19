from django.shortcuts import render, redirect
from django.views.generic import FormView
#
from applications.contact.models import Contact
from .forms import ContactForm
from .models import Msg

class ContactView(FormView):

    form_class = ContactForm
    template_name = 'contact/contact.html'

    def get(self, request, *args, **kwargs):

        last_contact_added = Contact.objects.get_last_contact()

        return render(request, self.template_name, {
            'form': self.form_class,
            'last_contact_added':last_contact_added
        })
    
    def form_valid(self, form):

        message = form.cleaned_data['message']
        contact_information = form.cleaned_data['contact']

        # verify number of message
        messages_number = Msg.objects.filter(contact_information=contact_information).count()

        if messages_number <= 3:    
            new_message = Msg()
            new_message.message = message
            new_message.contact_information = contact_information
            new_message.save()
            return redirect('contact_app:contact')
        else:
            return redirect('/')

