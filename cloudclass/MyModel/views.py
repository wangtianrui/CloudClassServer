from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.response import HttpResponse
from . import models
from django.views.decorators.csrf import csrf_exempt
import django.db.utils


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
        except Exception:
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
        except Exception:
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
        except Exception:
            print()
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})