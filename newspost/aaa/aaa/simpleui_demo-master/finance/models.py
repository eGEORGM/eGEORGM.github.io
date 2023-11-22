from django.db import models
from demo.models import *

# Create your models here.

class Record(models.Model):
    name = models.CharField(verbose_name='收支项', max_length=128, help_text='每一笔款项描述')
    money = models.DecimalField(verbose_name='金额', decimal_places=2, max_digits=9)
    create_date = models.DateTimeField(verbose_name='时间', auto_now=True)

    type_choices = (
        (0, '收入'),
        (1, '支出'),
    )
    type = models.IntegerField(verbose_name='类型', choices=type_choices)

    class Meta:
        verbose_name = "收支"
        verbose_name_plural = "收支记录"

    def __str__(self):
        return self.name


class Layer(Record):
    class Meta:
        verbose_name = "按钮弹出对话框"
        verbose_name_plural = "按钮弹出对话框"

class application(models.Model):
    name = models.CharField(max_length=128, verbose_name='名称', help_text="客户名称", null=False, blank=False,
                            db_index=True)
    industry = models.CharField(max_length=10, verbose_name='行业', blank=True, null=True)
    address = models.CharField(max_length=10, verbose_name='区域', blank=True, null=True)
    enable = models.BooleanField(verbose_name='状态', default=False)
    reason = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='违约原因',
                               db_index=True)
    level_choices = {
        (0, '低'),
        (1, '中'),
        (2, '高'),
    }
    applytime = models.DateTimeField(verbose_name='申请时间',default=timezone.now)
    level = models.IntegerField(choices=level_choices, verbose_name='严重程度', default=0)
    applyperson = models.CharField(max_length=10, verbose_name='认定人', blank=True, null=True)
    outerlevel_choices = {
        (0, '1'),
        (1, '2'),
        (2, '3'),
        (3, '4'),
        (4, '5'),
    }
    outerlevel = models.IntegerField(choices=outerlevel_choices, verbose_name='外部等级', default=0)
    remark =  models.CharField(max_length=128, verbose_name='备注', blank=True, null=True)

    class Meta:
        verbose_name = "认定审核"
        verbose_name_plural = "认定审核"

    def __str__(self):
        return self.name
class defaultperson(models.Model):
    name = models.CharField(max_length=128, verbose_name='名称', help_text="客户名称", null=False, blank=False,
                            db_index=True)
    industry= models.CharField(max_length=10, verbose_name='行业', blank=True, null=True)
    address = models.CharField(max_length=10, verbose_name='区域', blank=True, null=True)
    enable = models.BooleanField(verbose_name='状态', default=False)
    reason =models.ForeignKey(Department, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='违约原因',
                                   db_index=True)
    level_choices = {
        (0, '低'),
        (1, '中'),
        (2, '高'),
    }
    level = models.IntegerField(choices=level_choices, verbose_name='严重程度', default=0)
    applyperson = models.CharField(max_length=10, verbose_name='认定人', blank=True, null=True)
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
    # applytime = models.DateField(verbose_name='申请时间')
    # audittime = models.DateField(verbose_name='审核时间')
    class Meta:
        verbose_name = "重生审核"
        verbose_name_plural = "重生审核"

    def __str__(self):
        return self.name
