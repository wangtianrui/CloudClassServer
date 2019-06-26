from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
import django.db.utils
from django.forms.models import model_to_dict


# {"result": "该手机已注册"}
# Create your views here.
@csrf_exempt
def register(request):
    if request.method == "POST":
        # name = request.POST.get("name")
        phone = request.POST.get("phone")
        # sex = request.POST.get("sex")
        type = request.POST.get("type")
        # class_number = request.POST.get("classNumber")
        pass_word = request.POST.get("passWord")
        # academy = request.POST.get("academy")
        id_card = request.POST.get("idCard")
        try:
            user = models.User.objects.create(
                phone=phone,
                type=type,
                pass_word=pass_word,
                id_card=id_card
            )
            user.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def login(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        pass_word = request.POST.get("passWord")
        user = models.User.objects.filter(phone=phone)
        if user:
            if user.values()[0]["pass_word"] == pass_word:
                return JsonResponse({"result": 1})
            else:
                return JsonResponse({"result": 0})
        else:
            return JsonResponse({"result": -1})


@csrf_exempt
def complete_information(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        user = models.User.objects.get(phone=phone)
        name = request.POST.get("name")
        sex = request.POST.get("sex")
        class_number = request.POST.get("classNumber")
        academy = request.POST.get("academy")
        user.name = name
        user.sex = sex
        user.class_number = class_number
        user.academy = academy
        try:
            user.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
    return JsonResponse({"result": 1})


@csrf_exempt
def create_course(request):
    if request.method == "POST":
        name = request.POST.get("name")
        course_id = request.POST.get("courseId")
        invite_code = request.POST.get("inviteCode")
        creator_id = request.POST.get("creatorId")
        row = request.POST.get("rowNumber")
        col = request.POST.get("columnNumber")
        class_room_number = request.POST.get("classroomNumber")

        try:
            course = models.Course.objects.create(
                course_id=course_id,
                invite_code=invite_code,
                name=name,
                creator_id=creator_id,
                row_number=row,
                column_number=col,
                class_room_number=class_room_number
            )
            course.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def joinCourse(request):
    if request.method == "POST":
        student_id = request.POST.get("userId")
        course_id = request.POST.get("courseId")
        item_id = student_id + course_id

        try:
            item = models.Student2Course.objects.create(
                student_id=student_id,
                course_id=course_id,
                id=item_id
            )
            item.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def get_course(request):
    if request.method == "POST":
        user_id = request.POST.get("userId")
        courses = models.Student2Course.objects.filter(student_id=user_id)
        values = []
        for item in courses:
            values.append(model_to_dict(item))
        return JsonResponse({"result": len(values), "values": values})
    else:
        return JsonResponse({"result": 0})


@csrf_exempt
def create_inform(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")
        uper_id = request.POST.get("uperId")
        title = request.POST.get("title")
        content = request.POST.get("content")
        try:
            inform = models.Inform.objects.create(
                course_id=course_id,
                uper_id=uper_id,
                title=title,
                content=content
            )
            inform.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def get_inform(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")
        informs = models.Inform.objects.filter(course_id=course_id)
        inform_list = []
        for item in informs:
            temp = model_to_dict(item)
            temp["up_time"] = item.up_time
            inform_list.append(temp)
        return JsonResponse({"result": len(inform_list), "values": inform_list})
    else:
        return JsonResponse({"result": 0})
