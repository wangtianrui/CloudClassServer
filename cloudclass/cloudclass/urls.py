"""cloudclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
import MyModel.views as view
from django.conf.urls import url, include
from django.views.static import serve
from cloudclass.settings import MEDIA_ROOT
from cloudclass.settings import STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    re_path(r'register/$', view.register),
    re_path(r'login/$', view.login),
    re_path(r'complete_information/$', view.complete_information),
    re_path(r'create_course/$', view.create_course),
    re_path(r'joinCourse/$', view.joinCourse),
    re_path(r'get_course/$', view.get_course),
    re_path(r'create_inform/$', view.create_inform),
    re_path(r'get_inform/$', view.get_inform),
    re_path(r'add_avatar/$', view.add_avatar),
    re_path(r'add_source/$', view.add_source),
    re_path(r'get_source/$', view.get_source),

]
