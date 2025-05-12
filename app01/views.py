from django.shortcuts import render, HttpResponse, redirect
from app01.models import UserInfo

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def userList(request):
    
    name = "张三"
    userlist = ["张三", "李四", "王五"]
    context = {
        "name" : "张三",
        "salary" : 10000,
        "role" : "管理员"
    }
    
    return render(request, "user_list.html", {"n1":name, "n2":userlist, "context":context})

def userAdd(request):
    return HttpResponse("添加用户")


def login(request):
    method = request.method
    if method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == "admin" and password == "123456":
        return HttpResponse("登录成功")
    return render(request, "login.html", {"error_msg":"用户名或密码错误"})

from app01.models import Department

def orm(request):
    
    # 新建数据
    Department.objects.create(title="开发部")
    Department.objects.create(title="测试部")
    Department.objects.create(title="运维部")
    
    # 删除数据
    Department.objects.filter(id=1).delete()
    
    # 查看数据
    querySet = Department.objects.all()
    for obj in querySet:
        print(obj.id, obj.title)
        
    # 修改数据
    Department.objects.filter(title="测试部").update(title="游戏部")
    
    return HttpResponse("成功")

def infoList(request):
    dataList = UserInfo.objects.all()
    
    return render(request, "info_list.html", {"dataList":dataList})

def addList(request):
    if request.method == "GET":
        return render(request, "add_list.html")
    name = request.POST.get("name")
    password = request.POST.get("password")
    age = request.POST.get("age")
    UserInfo.objects.create(name=name, password=password, age=age)
    return redirect("/info/list")

def deleteList(request):
    if request.method == "GET":
        return render(request, "delete_list.html")
    id = request.POST.get("id")
    UserInfo.objects.filter(id=id).delete()
    return redirect("/info/list")

def editList(request):
    if request.method == "GET":
        return render(request, "edit_list.html")
    id = request.POST.get("id")
    name = request.POST.get("name")
    password = request.POST.get("password")
    age = request.POST.get("age")
    UserInfo.objects.filter(id=id).update(name=name, password=password, age=age)
    return redirect("/info/list")

