from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from contacts.models import Contact, Address, Sloonodaten
import urllib2
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
import forms
from django.http import HttpResponseRedirect, HttpResponse

class ListContactView(ListView):

    model = Contact
    template_name = 'contact_list.html'
    
    def get_success_url(self):
	return reverse('contacts-list')

class CreateContactView(CreateView):

	model = Contact
	template_name = 'edit_contact.html'
        form_class = forms.ContactForm         
  
	def get_success_url(self):
		return reverse('contacts-list')

class CreateContactView(CreateView):

    model = Contact
    template_name = 'edit_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')

        return context

class UpdateContactView(UpdateView):

    model = Contact
    template_name = 'edit_contact.html'
    form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')

    def get_context_data(self, **kwargs):

        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit', kwargs={'pk': self.get_object().id})

        return context

class SMSContactView(UpdateView):

    model = Contact
    template_name = 'sms_contact.html'
    form_class = forms.ContactForm

def sms_send(request):
	text = request.POST['sms_text']
	nummer = request.POST['sms_nummer']
        nummer_send = str(nummer).replace("0", "49", 1)
        text_send = text.replace(" ", "+")
	user = Sloonodaten.objects.get(pk=1)
	urllib2.urlopen("http://www.sloono.de/API/httpsms.php?user=" + user.user + "&password=" + user.pw + "&typ=1&text=" + text_send + "&to=%2B" + nummer_send).read()
	return HttpResponseRedirect('/')
	

class DeleteContactView(DeleteView):

    model = Contact
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')

class ContactView(DetailView):

	model = Contact
	template_name = 'contact.html'

class EditContactAddressView(UpdateView):

    model = Contact
    template_name = 'edit_addresses.html'
    form_class = forms.ContactAddressFormSet

    def get_success_url(self):

        # redirect to the Contact view.
        return self.get_object().get_absolute_url()
