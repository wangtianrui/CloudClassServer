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
    re_path(r'join_course/$', view.join_course),
    re_path(r'upSign/$', view.upSign),
    re_path(r'studentSign/$', view.studentSign),
    re_path(r'getSign/$', view.getSign),
    re_path(r'getSignedStudent/$', view.getSignedStudent),
    re_path(r'getCourseMember/$', view.getCourseMember),
    re_path(r'create_communication/$', view.create_communication),
    re_path(r'get_communication/$', view.get_communication),
    re_path(r'create_communicationitem/$', view.create_communicationitem),
    re_path(r'get_communicationitem/$', view.get_communicationitem),
    re_path(r'add_homework/$', view.add_homework),
    re_path(r'get_homework/$', view.get_homework),
    re_path(r'add_answer/$', view.add_answer),
    re_path(r'get_answer/$', view.get_answer),
    re_path(r'get_user/$', view.get_user),
    re_path(r'scoreAnswer/$', view.scoreAnswer),
    re_path(r'addScore/$', view.addScore),
    re_path(r'get_mean_score/$', view.get_mean_score),
    re_path(r'add_courseTable/$', view.add_courseTable),
    re_path(r'get_courseTable/$', view.get_courseTable),
    re_path(r'deleteCourseTable/$', view.deleteCourseTable),
    re_path(r'addPower/$', view.addPower),
    re_path(r'getPower/$', view.getPower),
    re_path(r'autoSeat/$', view.autoSeat),
    re_path(r'getSeat/$', view.getSeat),

]
