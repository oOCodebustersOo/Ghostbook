from django.contrib import admin
from contacts.models import Sloonodaten
from models import Contact
from forms import ContactForm

admin.site.register(Sloonodaten)
admin.site.register(Contact)
