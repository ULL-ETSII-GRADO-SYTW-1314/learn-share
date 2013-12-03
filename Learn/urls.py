from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Learn.views.home', name='home'),
    # url(r'^Learn/', include('Learn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^login/$', 'users.views.login_user', name='Login'),
    url(r'^home/$', 'users.views.home', name='home'),
    url(r'^logout/$', 'users.views.logout_user', name='Logout'),
    
    url(r'^registro/', 'users.views.register', name='registro'),
)
