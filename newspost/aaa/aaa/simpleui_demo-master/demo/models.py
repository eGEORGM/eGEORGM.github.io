from django.db import models
from django  import forms
# Create your models here.
from django.urls import reverse

from rate import fields
from django.db import migrations
from django.utils import timezone



class Department(models.Model):
    name = models.CharField(max_length=128, verbose_name='原因', help_text='违约原因应该唯一', unique=True, db_index=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    class Meta:
        verbose_name = "违约原因"
        verbose_name_plural = "违约原因"

    def __str__(self):
        return self.name


class RateModel(models.Model):
    f1 = fields.RateField(verbose_name='评分1', max_value=5)

    # 指定最大值，和允许选半格
    f2 = fields.RateField(verbose_name='评分2', max_value=5, allow_half=True, show_score=False)

    # disabled 设为默认读
    f3 = fields.RateField(verbose_name='评分3', max_value=5, default=3.5, disabled=True)

    class Meta:
        verbose_name = 'Rate评分'
        verbose_name_plural = 'Rate评分'


class Title(models.Model):
     name = models.CharField(max_length=128, verbose_name='原因', help_text='重生原因应该唯一', unique=True, db_index=True,default=' ')
     create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

     class Meta:
        verbose_name = "重生原因"
        verbose_name_plural = "重生原因"

     def __str__(self):
        return self.name



# class Image(models.Model):
#     image = models.ImageField(verbose_name='图片')
#     title = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, )
#
#     class Meta:
#         verbose_name = '图片'
#         verbose_name_plural = '图片管理'
#
#     def __str__(self):
#         return self.image.path


class employe(models.Model):
    name = models.CharField(max_length=128, verbose_name='名称', help_text="客户名称", null=False, blank=False,
                            db_index=True)
    industry = models.CharField(max_length=10, verbose_name='行业', blank=True, null=True)
    address = models.CharField(max_length=10, verbose_name='区域', blank=True, null=True)
    reason = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='违约原因',
                                   db_index=True)
    reamrk = models.CharField(max_length=128, verbose_name='备注', blank=True, null=True)
   
    class Meta:
        verbose_name = "违约申请"
        verbose_name_plural = "违约申请"

    def __str__(self):
        return self.name

class reborn_application(models.Model):
    name = models.CharField(max_length=128, verbose_name='名称', help_text="客户名称", null=False, blank=False,
                            db_index=True)
    industry= models.CharField(max_length=10, verbose_name='行业', blank=True, null=True)
    address = models.CharField(max_length=10, verbose_name='区域', blank=True, null=True)
    enable = models.BooleanField(verbose_name='状态', default=False)
    reason = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='违约原因',
                                   db_index=True)
    level_choices = {
        (0, '低'),
        (1, '中'),
        (2, '高'),
    }
    level = models.IntegerField(choices=level_choices, verbose_name='严重程度', default=0)
    applyperson = models.CharField(max_length=10, verbose_name='认定人', blank=False, null=True)
    outerlevel_choices = {
        (0, '1'),
        (1, '2'),
        (2, '3'),
        (3, '4'),
        (4, '5'),
    }
    outerlevel = models.IntegerField(choices=outerlevel_choices, verbose_name='外部等级', default=0)
    rebornreason = models.ForeignKey(Title, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='重生原因',
                                   db_index=True)
    applytime = models.DateTimeField(verbose_name='申请时间',default=timezone.now)
    audittime = models.DateTimeField(verbose_name='审核时间',default=timezone.now)
    class Meta:
        verbose_name = "重生申请"
        verbose_name_plural = "重生申请"

    def __str__(self):
        return self.name
class News(models.Model):
    title = models.CharField(max_length=200)
    uploadtime = models.DateField()
    context = models.TextField()
    type = models.CharField(max_length=100)
    image = models.ForeignKey('Image', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=200, default='Default Title')
    image = models.ImageField(upload_to='images/')  # 保存在 media/images/ 文件夹下

    def __str__(self):
        return self.title