from django.contrib import admin
from MyModel.models import *

# Register your models here.

admin.site.register([User, Course, Student2Course, Inform, HomeWork, Answer, Communication, CommunicaitonItem,
                     Sign, StudentSign, Score, MySource, CourseModel, Power, Seat])
