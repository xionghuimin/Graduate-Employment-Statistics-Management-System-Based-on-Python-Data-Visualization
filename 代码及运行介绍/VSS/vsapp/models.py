from django.db import models
# Create your models here.
class Student(models.Model):
    grade = models.CharField(max_length=50)  # 年级
    number = models.CharField(max_length=50)  # 学号
    name = models.CharField(max_length=50) #名字
    sex = models.CharField(max_length=20)#性别
    major = models.CharField(max_length=50) #专业
    target = models.CharField(max_length=500)#就业情况：工作、考研、考公或事业单位、参军、其他
    situation = models.CharField(max_length=200)#就业结果：成功或失败，0/1
    later = models.CharField(max_length=500)#接下来的就业计划：工作、考研、考公或事业单位、其他
    position = models.CharField(max_length=500)#工作岗位
    province = models.CharField(max_length=500) # 毕业后去往的省份
    city = models.CharField(max_length=500) # 毕业后去往的城市
    AnnualSalary = models.CharField(max_length=500) # 工作年薪