from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'staticsite.views.index', name='index'),
    
    #OLD CONTACT PAGE THAT DIDN'T WORK
    #url(r'^contact/$', 'staticsite.views.contact', name='contact'),
    #url(r'^contact/submit/$', 'staticsite.views.contactSubmit', name='contectSubmitted'),

    url(r'^contact/$', 'contactPage.views.contact', name='contact'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
