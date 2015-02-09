from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
<<<<<<< HEAD
    # url(r'^blog/', include('blog.urls')),
=======
    url(r'^blog/', include('blog.urls')),
>>>>>>> test

    url(r'^admin/', include(admin.site.urls)),
)
