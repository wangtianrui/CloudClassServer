from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models
from django.shortcuts import render_to_response
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def saveTest(request):
    temp = models.Test(name="哈哈哈")
    temp.save()
    return HttpResponse("添加成功")


def queryTest(request):
    response = ""
    list = models.Test.objects.all()
    for item in list:
        response += item.name
    return HttpResponse("<p>" + response + "111</p>")


def openHtml(request):
    return render_to_response(r"seach.html")


@csrf_exempt
def search(request):
    #
    print(request.method)
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        sex = request.POST.get("sex")

    data = {
        "name": name,
        "age": age,
        "sex": "sdas"
    }
    print(data)
    return JsonResponse(data)
