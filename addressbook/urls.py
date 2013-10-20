from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import contacts.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  
     url(r'^$', contacts.views.ListContactView.as_view(),
         name='contacts-list',),

     url(r'^new$', contacts.views.CreateContactView.as_view(),
         name='contacts-new',),

     url(r'^edit/(?P<pk>\d+)/$', contacts.views.UpdateContactView.as_view(),
        name='contacts-edit',),

     url(r'^sms/(?P<pk>\d+)/$', contacts.views.SMSContactView.as_view(),
        name='contacts-sms',),

	 url(r'^calendarsms/', include('calendar_sms.urls')),

     url(r'^contacts/sms_send/$', contacts.views.sms_send, name='sms_send'),
    
     url(r'^delete/(?P<pk>\d+)/$', contacts.views.DeleteContactView.as_view(),
        name='contacts-delete',),
     
     url(r'^(?P<pk>\d+)/$', contacts.views.ContactView.as_view(),
        name='contacts-view',),
    
     url(r'^edit/(?P<pk>\d+)/addresses$', contacts.views.EditContactAddressView.as_view(),
        name='contacts-edit-addresses',),

     url(r'^accounts/', include('registration.backends.default.urls')),
    # Examples:
    # url(r'^$', 'addressbook.views.home', name='home'),
    # url(r'^addressbook/', include('addressbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()


