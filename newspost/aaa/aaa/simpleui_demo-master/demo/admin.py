import datetime
from datetime import date
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts import options as opts
import pandas as pd
import time
from django.contrib import admin, messages
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse
import os
from simpleui import forms
from simpleui.admin import AjaxAdmin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from django.core import serializers
# from finance.models import application,defaultperson
from django.http import FileResponse
from django.conf import settings
from pyecharts.charts import Grid
# Register your models here.
# @admin.register(Department)
# class DepartmentAdmin(admin.ModelAdmin):
#     # 要显示的字段
#     list_display = ('id', 'name')
#
#     # 需要搜索的字段
#     search_fields = ('name',)
#
#     # 分页显示，一页的数量
#     list_per_page = 10
#
#     actions_on_top = True
# @admin.register(Title)
# class Title(admin.ModelAdmin):
#     list_display=('id', 'name')
#
#     # 需要搜索的字段
#     search_fields = ('name',)
#
#     # 分页显示，一页的数量
#     list_per_page = 10
#
#     actions_on_top = True

class AgeListFilter(admin.SimpleListFilter):
    title = u'最近生日'
    parameter_name = 'ages'

    def lookups(self, request, model_admin):
        return (
            ('0', u'最近7天'),
            ('1', u'最近15天'),
            ('2', u'最近30天'),
        )

    def queryset(self, request, queryset):
        # 当前日期格式
        cur_date = datetime.datetime.now().date()

        if self.value() == '0':
            # 前一天日期
            day = cur_date - datetime.timedelta(days=1)

            return queryset.filter(birthday__gte=day)
        if self.value() == '1':
            day = cur_date - datetime.timedelta(days=15)
            return queryset.filter(birthday__gte=day)
        if self.value() == '2':
            day = cur_date - datetime.timedelta(days=30)
            return queryset.filter(birthday__gte=day)

class ProxyResource(resources.ModelResource):
    class Meta:
        model = employe

# @admin.register(employe)
# class applicationAdmin(ImportExportActionModelAdmin, AjaxAdmin):
#     resource_class = ProxyResource
#     list_display = ( 'name', 'industry', 'address','reason','reamrk')#,  'create_time'
#     # search_fields = ('name', 'enable', 'idCard', 'department')
#     list_editable = ('reason','reamrk')
#     raw_id_fields = ('reason', )
#     search_fields = ('name','industry', 'address')
#     list_per_page = 20
#     # raw_id_fields = ('reason',)
#     # list_filter = ('reason',)
#     # list_filter = (AgeListFilter, 'department', 'create_time', 'birthday', 'time', 'enable', 'gender')
#     # list_filter = (AgeListFilter,'name')
#     # list_editable= ('name',)
#     list_display_links = ('name',)
#     actions=['test','test1']
#     def test(self, request, queryset):
#         ids = request.POST.getlist('_selected_action')
#         for id in ids:
#             application1 = employe.objects.get(id=id)
#             application.objects.create(
#                 name=application1.name,
#                 address=application1.address,
#                 reason_id=application1.reason.id,
#                 enable = False,
#                 remark = application1.reamrk,
#                 applyperson = request.user,
#                 industry = application1.industry
#             )
#             employe.objects.get(id=id).delete()
#
#         messages.add_message(request, messages.SUCCESS, '提交成功'.format(len(ids)))
#
#     test.short_description='提交'
#
#     # 自 3.4+ 支持confirm确认提示
#     test.confirm = '您确定要提交这些认定吗？'
#
#     @transaction.atomic
#     def test1(self, request, queryset):
#         h1=0
#         h2=0
#         h3=0
#         h4=0
#         h5=0
#         h6=0
#         h7=0
#         q1=0
#         q2=0
#         q3=0
#         q4=0
#         q5=0
#         ids1=request.POST.getlist('_selected_action')
#         for id in ids1:
#             Employe= employe.objects.get(id=id)
#             if Employe.industry=='教育':
#                 h1=h1+1
#             if Employe.industry=='科技':
#                 h2=h2+1
#             if Employe.industry=='金融':
#                 h3=h3+1
#             if Employe.industry=='制造':
#                 h4=h4+1
#             if Employe.industry=='艺术':
#                 h5=h5+1
#             if Employe.industry=='能源':
#                 h6=h6+1
#             if Employe.industry=='贸易':
#                 h7=h7+1
#             if Employe.address=='东部':
#                 q1=q1+1
#             if Employe.address=='西部':
#                 q2=q2+1
#             if Employe.address=='南部':
#                 q3=q3+1
#             if Employe.address=='东北':
#                 q4=q4+1
#             if Employe.address=='中部':
#                 q5=q5+1
#         df1 = pd.DataFrame({"行业":["教育","科技","金融","制造","艺术","能源","贸易"],"数据":[h1,h2,h3,h4,h5,h6,h7]})
#         df2 = pd.DataFrame({"区域":["东部","西部","南部","东北","中部"],"数据":[q1,q2,q3,q4,q5]})
#         c = (
#         Bar(init_opts=opts.InitOpts(width="1700px",height="750px",))
#         .add_xaxis(df1["行业"].tolist())
#         .add_yaxis("行业",df1["数据"].tolist())
#         .set_global_opts(title_opts=opts.TitleOpts(title=""),legend_opts=opts.LegendOpts(is_show=False))
#         )
#         d=(
#         Bar()
#         .add_xaxis(df2["区域"].tolist())
#         .add_yaxis("区域",df2["数据"].tolist())
#         .set_global_opts(title_opts=opts.TitleOpts(title=""),legend_opts=opts.LegendOpts(is_show=False))
#         )
#         a=(
#             Pie()
#             .add("",[list(z)for z in zip(df1['行业'],df1['数据'])],center=["25%","25%"],radius=["25%","50%"],rosetype="radius")
#             .set_global_opts(title_opts=opts.TitleOpts(title=""),legend_opts=opts.LegendOpts(is_show=False))
#         )
#         b=(
#             Pie()
#             .add("",[list(z)for z in zip(df2['区域'],df2['数据'])],radius=["25%","50%"],center=["75%","25%"],rosetype="radius")
#             .set_global_opts(title_opts=opts.TitleOpts(title=""),legend_opts=opts.LegendOpts(is_show=False))
#         )
#         grid = (
#
#         Grid()
#         .add(c,grid_opts=opts.GridOpts(pos_top="60%", pos_left="60%"))
#         .add(d,grid_opts=opts.GridOpts(pos_top="60%", pos_right="60%"))
#         .add(a,grid_opts=opts.GridOpts(pos_bottom="60%", pos_left="60%"))
#         .add(b,grid_opts=opts.GridOpts(pos_bottom="60%", pos_right="60%"))
#         .render('chongsheng.html'))
#     test1.short_description='生成图'

@admin.register(News)
class news(ImportExportActionModelAdmin, AjaxAdmin):
    resource_class = ProxyResource
    list_display = (
   'title','uploadtime','type','image')
    search_fields = (
   'title','uploadtime','context','type','image')
    list_per_page = 20
    raw_id_fields = ('image',)
    list_select_related = ('image',)  # 优化数据库查询

    save_on_top = True
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title', 'image')

# @admin.register(reborn_application)
# class rebornAdmin(ImportExportActionModelAdmin, AjaxAdmin):
#     resource_class = ProxyResource
#     list_display = ( 'name', 'industry', 'address', 'enable','reason', 'level', 'outerlevel','rebornreason', 'applyperson','applytime','audittime')
#     search_fields = ('name', 'industry', 'address','reason', 'level', 'outerlevel','applyperson')
#     # list_editable = ('rebronreason',)
#     # search_fields = ('name')
#     list_per_page = 20
#     # raw_id_fields = ('reason')
#     # list_filter = ('reason')
#     # list_filter = (AgeListFilter, 'department', 'create_time', 'birthday', 'time', 'enable', 'gender')
#     raw_id_fields = ('reason', 'rebornreason')
#     list_display_links = ('name',)
#     list_editable = ('rebornreason',)
#
#
#     save_on_top = True
#
#     @transaction.atomic
#     def test(self, request, queryset):
#         ids = request.POST.getlist('_selected_action')
#         for id in ids:
#             application1 = reborn_application.objects.get(id=id)
#             defaultperson.objects.create(
#                 name=application1.name,
#                 address=application1.address,
#                 reason_id=application1.reason.id,
#                 enable = False,
#                 rebornreason_id =application1.rebornreason.id,
#                 applyperson = request.user,
#                 industry = application1.industry
#             )
#             reborn_application.objects.get(id=id).delete()
#
#         messages.add_message(request, messages.SUCCESS, '提交成功'.format(len(ids)))
#
#     test.short_description='提交'
#
#     # 自 3.4+ 支持confirm确认提示
#     test.confirm = '您确定要提交这些认定吗？'
#     def test1(self, request, queryset):
#         h1=0
#         h2=0
#         h3=0
#         h4=0
#         h5=0
#         h6=0
#         h7=0
#         q1=0
#         q2=0
#         q3=0
#         q4=0
#         q5=0
#         ids1=request.POST.getlist('_selected_action')
#         for id in ids1:
#             Employe= reborn_application.objects.get(id=id)
#             if Employe.industry=='教育':
#                 h1=h1+1
#             if Employe.industry=='科技':
#                 h2=h2+1
#             if Employe.industry=='金融':
#                 h3=h3+1
#             if Employe.industry=='制造':
#                 h4=h4+1
#             if Employe.industry=='艺术':
#                 h5=h5+1
#             if Employe.industry=='能源':
#                 h6=h6+1
#             if Employe.industry=='贸易':
#                 h7=h7+1
#             if Employe.address=='东部':
#                 q1=q1+1
#             if Employe.address=='西部':
#                 q2=q2+1
#             if Employe.address=='南部':
#                 q3=q3+1
#             if Employe.address=='东北':
#                 q4=q4+1
#             if Employe.address=='中部':
#                 q5=q5+1
#         df1 = pd.DataFrame({"行业":["教育","科技","金融","制造","艺术","能源","贸易"],"数据":[h1,h2,h3,h4,h5,h6,h7]})
#         df2 = pd.DataFrame({"区域":["东部","西部","南部","东北","中部"],"数据":[q1,q2,q3,q4,q5]})
#         c = (
#         Bar()
#         .add_xaxis(df1["行业"].tolist())
#         .add_yaxis("行业",df1["数据"].tolist())
#         .set_global_opts(title_opts=opts.TitleOpts(title=""),legend_opts=opts.LegendOpts(is_show=False))
#         )
#         d=(
#         Bar()
#         .add_xaxis(df2["区域"].tolist())
#         .add_yaxis("区域",df2["数据"].tolist())
#         .set_global_opts(title_opts=opts.TitleOpts(title=""),legend_opts=opts.LegendOpts(is_show=False))
#         )
#         a=(
#             Pie()
#             .add("",[list(z)for z in zip(df1['行业'],df1['数据'])],radius=["25%","50%"],center=["25%","25%"],rosetype="radius")
#             .set_global_opts(title_opts=opts.TitleOpts(title=""),legend_opts=opts.LegendOpts(is_show=False))
#         )
#         b=(
#             Pie()
#             .add("",[list(z)for z in zip(df2['区域'],df2['数据'])],radius=["25%","50%"],center=["75%","25%"],rosetype="radius")
#             .set_global_opts(title_opts=opts.TitleOpts(title=""),legend_opts=opts.LegendOpts(is_show=False))
#         )
#         grid = (
#
#         Grid()
#         .add(c,grid_opts=opts.GridOpts(pos_top="60%", pos_left="60%"))
#         .add(d,grid_opts=opts.GridOpts(pos_top="60%", pos_right="60%"))
#         .add(a,grid_opts=opts.GridOpts(pos_bottom="60%", pos_left="60%"))
#         .add(b,grid_opts=opts.GridOpts(pos_bottom="60%", pos_right="60%"))
#         .render('weiyue.html')
#         )
#
#     # 自 3.4+ 支持confirm确认提示
#     test1.short_description='生成图'
#
#     # 增加自定义按钮
#     actions = ['test', 'test1']

   