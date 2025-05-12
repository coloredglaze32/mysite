# Django项目

## 创建项目

### 使用终端

* 打开终端
* 进入某个目录

```python
django-admin startproject 项目名称
```

### 使用Pycharm

* 新建时勾选Django即可

## 项目结构

```python
mysite
|----manage.py           [项目的管理，启动项目，创建app、数据管理][不要动]
|----mysite
     |----__init__.py
     |----settings.py    [项目配置][常常操作]
     |----urls.py        [URL和函数的对应关系][常常操作]
     |----asgi.py        [接收网络请求]
     |----wsgi.py        [接收网络请求]
```

## APP

```python
- 项目
    -app, 用户管理【表结构，函数，HTML模板，CSS】
    -app, 订单管理【表结构，函数，HTML模板，CSS】
    -app, 后台管理【表结构，函数，HTML模板，CSS】
    -app, 网站【表结构，函数，HTML模板，CSS】
    -app, API【表结构，函数，HTML模板，CSS】

注意：我们开发比较简洁，用不到多app，一般情况下，项目下创建1个app即可
```

```

python manage.py startapp app01

E:.
│  manage.py
│  README.md
│  
├─app01
│  │  admin.py         [固定，不用动]django默认提供了admin后台管理。
│  │  apps.py          [固定，不用动]app启动类
│  │  models.py        [重要]，对数据库操作。
│  │  tests.py         [固定，不用动]单元测试
│  │  views.py         [重要]，函数。
│  │  __init__.py
│  │
│  └─migrations        [固定，不用动]数据库变更记录
│          __init__.py
│
└─mysite
    │  asgi.py
    │  settings.py
    │  urls.py         [URL->函数]
    │  wsgi.py
    │  __init__.py
    │
    └─__pycache__
            settings.cpython-311.pyc
            __init__.cpython-311.pyc
```

## 快速上手

### 确保app已经注册

```
/mysite/settings.py中INSTALLED_APPS（33行处）添加app

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01.apps.App01Config',
]
```

### 编写URL和视图函数对应关系

* urls.py

```python
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
]
```

* views.py

```python
from django.shortcuts import render

# Create your views here.
# 参数中必须写request
def index(request):
    return HttpResponse("Hello World")
```

### 启动项目

```
python manage.py runserver
```

### 再写一个页面

* urls.py

```python
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path("user/list/", views.userList),
]

```

* views.py

```python
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def userList(request):
    return HttpResponse("用户列表")

def userAdd(request):
    return HttpResponse("添加用户")
```

### templates

* 为了使用html文件，而不是使用HttpResponse，在app下新建templates

### 静态文件

需要在具体的app下新建目录static，存放图片，css，js等代码

* 引用静态文件(在html顶部添加)

```html
{$ load static $}
```

## 语法

* views.py中传参使用字典的方式
* 对应的html文件中如果直接使用变量，使用两个大括号包裹起来即可{{}}, 如果其中有函数，需要用{%  function %}这种方式

```python
def userList(request):
  
    name = "张三"
    userlist = ["张三", "李四", "王五"]
    context = {
        "name" : "张三",
        "salary" : 10000,
        "role" : "管理员"
    }
  
    return render(request, "user_list.html", {"n1":name, "n2":userlist, "context":context})
```

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>用户列表</h1>
    <img src="{% static '下载.png' %}" style="width: 100px;">

    <hr/>
  
    <h1>{{ n1 }}</h1>
    <h1>{{ n2.0 }}</h1>
    <h1>{{ n2.1 }}</h1>
    <h1>{{ n2.2 }}</h1>

    <h1>{{ context.name }}</h1>
    <h1>{{ context.salary }}</h1>
    <h1>{{ context.role }}</h1>


    <hr/>

    <div>
        {% for item in n2 %}
            <span>{{ item }}</span>
        {% endfor %}
    </div>

    <ul>
        {% for k,v in context.items %}
            <li>{{ k }} : {{ v }}</li>
        {% endfor %}
    </ul>

</body>

```

## 关于views.py中的参数request

* request是一个对象，封装了用户发送过来的所有请求相关数据

```python
# 1.获取请求方式 GET/POST
print(requese.method) 

# 2.重定向
return redirect("www.baidu.com")
```

## CSRF是什么

* Django 内置了 CSRF 防护机制。它会为每个用户会话生成一个唯一的 token（令牌），并要求每个 POST 表单都带上这个 token。服务器收到请求时会校验 token 是否正确。

```html
<form action="/login/" method="post">
        {% csrf_token %}
        <input type="text" name="username" placeholder="请输入用户名">
        <input type="password" name="password" placeholder="请输入密码">
        <input type="submit" value="登录">
</form>

<!-- 渲染后会变成 -->

<form method="post">
    <input type="hidden" name="csrfmiddlewaretoken" value="随机字符串">
    <input type="text" name="username" placeholder="请输入用户名">
    <input type="password" name="password" placeholder="请输入密码">
    <input type="submit" value="登录">
</form>
```

## 数据库操作

### 安装库

```html
pip install mysqlclient
```

### ORM

ORM可以做两件事：

创建、修改、删除数据库中的表（不用写SQL语句）无法创建数据库；操作表中的数据

* 配置数据库（settings.py）

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "django_db",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

* 连接数据库
  * 创建表

    ```python
    # model.py

    from django.db import models

    class UserInfo(model.Model):
        name = models.CharField(max_length=32)
        password = models.CharField(max_length=64)
        age = models.IntegerField()

    """
    等价于在数据库中执行如下语句
    create table app01_userinfo(
        id bigint auto_increment primary key,
        name varchar(32) not null,
        password varchar(64) not null,
        age int not null
    )
    """
    ```

    执行命令

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
  * 删除表
  * 修改表

## 案例（用户登录）
