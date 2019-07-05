from django.db import models


# Create your models here.

class User(models.Model):
    # 主键为phone
    phone = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=5)
    type = models.IntegerField()
    class_number = models.CharField(max_length=20)
    pass_word = models.CharField(max_length=20)
    academy = models.CharField(max_length=20)
    id_card = models.CharField(max_length=20)
    avatar = models.FileField(upload_to="media", default="media/default.jpg")


class Course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    invite_code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    creator_id = models.CharField(max_length=20)
    row_number = models.IntegerField()
    column_number = models.IntegerField()
    class_room_number = models.CharField(max_length=20)
    section = models.IntegerField(null=True)
    span = models.IntegerField(null=True)
    week = models.IntegerField(null=True)


class Student2Course(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    student_id = models.CharField(max_length=20)
    course_id = models.CharField(max_length=20)


class Inform(models.Model):
    course_id = models.CharField(max_length=20)
    uper_id = models.CharField(max_length=20)
    up_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)


class HomeWork(models.Model):
    course_id = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    up_time = models.DateTimeField(auto_now_add=True)
    uper_id = models.CharField(max_length=20)


class Answer(models.Model):
    homework_id = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    image = models.FileField(upload_to="media/answers", default="media/home_work_default.jpg")
    uper_id = models.CharField(max_length=20)
    up_time = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=-1)


class Communication(models.Model):
    course_id = models.CharField(max_length=20)
    uper_id = models.CharField(max_length=20)
    up_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, default="")
    content = models.CharField(max_length=300, default="")


class CommunicaitonItem(models.Model):
    uper_id = models.CharField(max_length=20)
    communication_id = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    up_time = models.DateTimeField(auto_now_add=True, null=True)


class Sign(models.Model):
    sign_code = models.CharField(max_length=10, primary_key=True)
    up_time = models.DateTimeField(auto_now_add=True)
    course_id = models.CharField(max_length=20)


class StudentSign(models.Model):
    sign_id = models.CharField(max_length=20)
    up_time = models.DateTimeField(auto_now_add=True)
    student_id = models.CharField(max_length=20)
    id = models.CharField(max_length=50, primary_key=True)


class Score(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    course_id = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    score = models.FloatField()


class MySource(models.Model):
    source_path = models.FileField(upload_to="media/source")
    course_id = models.CharField(max_length=20)
    type = models.IntegerField()
    uper_id = models.CharField(max_length=20)
    download_count = models.IntegerField(default=0)
    source_name = models.CharField(max_length=100, null=True)
    uper_name = models.CharField(max_length=20, null=True)


class CourseModel(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    section = models.IntegerField()
    week = models.IntegerField()
    span = models.IntegerField()
    user_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=40)
    classroom_number = models.CharField(max_length=20)


class Power(models.Model):
    student_id = models.CharField(max_length=20)
    level = models.IntegerField()
    status = models.CharField(max_length=20)
    time = models.IntegerField()
    course_id = models.CharField(max_length=20)


class Seat(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    row = models.IntegerField()
    col = models.IntegerField()
    courseId = models.CharField(max_length=20)
    studentId = models.CharField(max_length=20)


class Admin(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=30)
