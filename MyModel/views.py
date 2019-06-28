from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import models


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
        user_infor = {}
        if user:
            if user.values()[0]["pass_word"] == pass_word:
                for key in user.values()[0]:
                    user_infor[key] = user.values()[0][key]
                print(user_infor)
                return JsonResponse({"result": 1, "values": user_infor})
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
def join_course(request):
    if request.method == "POST":
        invite_code = request.POST.get("inviteCode")
        student_id = request.POST.get("studentId")
        try:
            course = models.Course.objects.get(invite_code=invite_code)
            course_id = model_to_dict(course)["course_id"]
            item_id = student_id + course_id
            student2course = models.Student2Course.objects.create(
                student_id=student_id,
                course_id=course_id,
                id=item_id
            )
            student2course.save()
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
            values.append(model_to_dict(models.Course.objects.get(course_id=model_to_dict(item)["course_id"])))
        return JsonResponse({"result": len(values), "values": values})
    else:
        return JsonResponse({"result": 0})


@csrf_exempt
def getCourseMember(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")

        student2courses = models.Student2Course.objects.filter(course_id=course_id)
        values = []
        for item in student2courses.values():
            student = models.User.objects.filter(phone=item["student_id"])
            temp = {}
            if student.values()[0]["type"] == 1:
                continue
            for key in student.values()[0]:
                temp[key] = student.values()[0][key]
            values.append(temp)
        return JsonResponse({"result": len(values), "values": values})
    else:
        return JsonResponse({"result": -1})


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


@csrf_exempt
def add_avatar(request):
    if request.method == "POST":
        avatar = request.FILES.get("avatar")
        user_id = request.POST.get("userId")

        user = models.User.objects.get(phone=user_id)
        user.avatar = avatar
        try:
            user.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def add_source(request):
    if request.method == "POST":
        source = request.FILES.get("source")
        course_id = request.POST.get("courseId")
        type = request.POST.get("type")
        uper_id = request.POST.get("uperId")
        source_name = request.POST.get("sourceName")
        uper_name = request.POST.get("uperName")
        course = models.Course.objects.get(course_id=course_id)
        if course:
            try:
                my_source = models.MySource.objects.create(
                    source_path=source,
                    course_id=course_id,
                    type=type,
                    uper_id=uper_id,
                    source_name=source_name,
                    uper_name=uper_name
                )
                my_source.save()
            except Exception as e:
                print(e)
                return JsonResponse({"result": 0})
            src = {
                "source_path": "media/source/" + str(source),
                "course_id": course_id,
                "uper_id": uper_id,
                "type": type
            }
            return JsonResponse({"result": 1, "values": src})
        else:
            return JsonResponse({"result": -1})


@csrf_exempt
def get_source(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")
        sources = models.MySource.objects.filter(course_id=course_id)

        srcs = []
        for item in sources.values():
            print(item)
            temp = {}
            for key in item:
                temp[key] = item[key]
            srcs.append(temp)
        return JsonResponse({"result": len(srcs), "values": srcs})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def upSign(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")
        sign_code = request.POST.get("signCode")

        try:
            sign = models.Sign.objects.create(
                course_id=course_id,
                sign_code=sign_code
            )
            sign.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def studentSign(request):
    if request.method == "POST":
        sign_code = request.POST.get("signCode")
        student_id = request.POST.get("studentId")
        id = sign_code + student_id
        sign = models.Sign.objects.filter(sign_code=sign_code)
        if sign:
            try:
                studentsign = models.StudentSign.objects.create(
                    sign_id=sign_code,
                    student_id=student_id,
                    id=id
                )
                studentsign.save()
            except Exception as e:
                print(e)
                return JsonResponse({"result": 0})
            return JsonResponse({"result": 1})
        else:
            return JsonResponse({"result": -2})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def getSign(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")

        try:
            signs = models.Sign.objects.filter(course_id=course_id)
            values = []
            for item in signs:
                temp = model_to_dict(item)
                temp["up_time"] = item.up_time
                values.append(temp)

            return JsonResponse({"result": len(values), "values": values})
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def getSignedStudent(request):
    if request.method == "POST":
        sign_code = request.POST.get("signCode")

        try:
            studentsigns = models.StudentSign.objects.filter(sign_id=sign_code)
            values = []
            for item in studentsigns:
                student = models.User.objects.filter(phone=item.student_id)
                temp = {}
                for key in student.values()[0]:
                    temp[key] = student.values()[0][key]
                values.append(temp)
            return JsonResponse({"result": len(values), "values": values})
        except Exception as e:
            print(e)
        return JsonResponse({"result": 0})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def create_communication(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")
        uper_id = request.POST.get("uperId")
        title = request.POST.get("title")
        content = request.POST.get("content")
        try:
            communication = models.Communication.objects.create(
                course_id=course_id,
                uper_id=uper_id,
                title=title,
                content=content
            )
            communication.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def get_communication(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")
        try:
            communications = models.Communication.objects.filter(course_id=course_id)
            values = []
            for item in communications.values():
                temp = {}
                for key in item:
                    temp[key] = item[key]
                # temp["up_time"] = item["up_time"]
                print(temp)
                user = models.User.objects.filter(phone=item["uper_id"]).values()[0]
                temp["user_type"] = user["type"]
                temp["user_name"] = user["name"]
                values.append(temp)
            return JsonResponse({"result": len(values), "values": values})
        except ImportError as e:
            print(e)
        return JsonResponse({"result": 0})

    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def create_communicationitem(request):
    if request.method == "POST":
        uper_id = request.POST.get("uperId")
        communication_id = request.POST.get("communication_id")
        content = request.POST.get("content")

        try:
            item = models.CommunicaitonItem.objects.create(
                uper_id=uper_id,
                communication_id=communication_id,
                content=content
            )
            item.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def get_communicationitem(request):
    if request.method == "POST":
        communication_id = request.POST.get("communication_id")

        items = models.CommunicaitonItem.objects.filter(communication_id=communication_id)
        values = []
        for item in items:
            temp = model_to_dict(item)
            temp["up_time"] = item.up_time
            user = models.User.objects.filter(phone=temp["uper_id"]).values()[0]
            temp["user_type"] = user["type"]
            temp["user_name"] = user["name"]
            values.append(temp)
        return JsonResponse({"result": len(values), "values": values})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def add_homework(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")
        title = request.POST.get("title")
        content = request.POST.get("content")
        uper_id = request.POST.get("userId")

        try:
            homework = models.HomeWork.objects.create(
                course_id=course_id,
                title=title,
                content=content,
                uper_id=uper_id
            )
            homework.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def get_homework(request):
    if request.method == "POST":
        course_id = request.POST.get("courseId")

        homeworks = models.HomeWork.objects.filter(course_id=course_id)

        values = []
        for item in homeworks:
            temp = model_to_dict(item)
            temp["up_time"] = item.up_time
            values.append(temp)

        return JsonResponse({"result": len(values), "values": values})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def add_answer(request):
    if request.method == "POST":
        homework_id = request.POST.get("homework_id")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        uper_id = request.POST.get("userId")

        try:
            answer = models.Answer.objects.create(
                homework_id=homework_id,
                content=content,
                image=image,
                uper_id=uper_id
            )
            answer.save()
        except Exception as e:
            print(e)
            return JsonResponse({"result": 0})
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def get_answer(request):
    if request.method == "POST":
        homework_id = request.POST.get("homework_id")

        answers = models.Answer.objects.filter(homework_id=homework_id)

        values = []
        for item in answers.values():
            temp = {}
            for key in item:
                temp[key] = item[key]
            values.append(temp)
        return JsonResponse({"result": len(values), "values": values})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def get_user(request):
    if request.method == "POST":
        id = request.POST.get("userId")
        user = models.User.objects.filter(phone=id).values()[0]
        temp = {}
        for key in user:
            temp[key] = user[key]
        return JsonResponse({"result": 1, "values": temp})


@csrf_exempt
def scoreAnswer(request):
    if request.method == "POST":
        id = request.POST.get("answerId")
        score = request.POST.get("score")
        answer = models.Answer.objects.get(id=id)
        answer.score = score
        answer.save()
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def addScore(request):
    if request.method == "POST":
        id = request.POST.get("id")
        score = request.POST.get("score")
        course_id = request.POST.get("courseId")
        user_id = request.POST.get("userId")

        temp = models.Score.objects.filter(id=id)
        if temp:
            temp = models.Score.objects.get(id=id)
            temp.score = score
            temp.save()
        else:
            score = models.Score.objects.create(
                id=id,
                score=score,
                course_id=course_id,
                student_id=user_id
            )
            score.save()
        return JsonResponse({"result": 1})
    else:
        return JsonResponse({"result": -1})


@csrf_exempt
def get_mean_score(request):
    if request.method == "POST":
        id = request.POST.get("studentId")

        num = 0.0
        sum = 0.0
        scores_list = models.Score.objects.filter(student_id=id)
        for item in scores_list:
            sum += item.score
            num += 1.0
            print(sum)
            print(num)
        if num == 0:
            num = 1
        return JsonResponse({"result": 1, "values": sum / num})
    else:
        return JsonResponse({"result": -1})
