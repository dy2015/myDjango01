"""myDjango01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01.views import index
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^app01/uid(\d+)name(\w+)/$', 'app01.views.index'),
    url(r'^app01/(?P<uid>\d{2})/$', index),
    url(r'^app01/regist/$', 'app01.views.regist'),
    
    url(r'^app02/regist/$', 'app02.views.regist'),
    url(r'^app02/login/$', 'app02.views.login'),
    url(r'^app02/index/$', 'app02.views.index'),
    
    url(r'^session/login/$', 'session.views.login'),  
    url(r'^session/index/$', 'session.views.index'), 
    url(r'^session/logout/$', 'session.views.logout'), 
]
