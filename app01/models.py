from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    
"""
create table app01_userinfo(
    id bigint auto_increment primary key,
    name varchar(32) not null,
    password varchar(64) not null,
    age int not null
)
"""

class Department(models.Model):
    title = models.CharField(max_length=32)
    

