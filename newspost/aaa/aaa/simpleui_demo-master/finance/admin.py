from django.contrib import admin
from django.http import JsonResponse
from django.db import transaction
from finance.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from simpleui.admin import AjaxAdmin
from django.contrib import admin, messages
from django.db import transaction
from django.http import JsonResponse
from django.urls import reverse


class ProxyResource(resources.ModelResource):
    class Meta:
        model = application
    
@admin.register(application)
class aply(ImportExportActionModelAdmin, AjaxAdmin):
    resource_class = ProxyResource
    list_display = ( 'name', 'industry', 'address','enable','outerlevel','reason','level','applyperson','remark')
    search_fields = ('name', 'industry', 'address','reason','level','applyperson')
    raw_id_fields = ('reason',)
    # search_fields = ('name')
    list_per_page = 20
   
    def test(self, request, queryset):
        ids = request.POST.getlist('_selected_action')
        for id in ids:
            application1 = application.objects.get(id=id)
            reborn_application.objects.create(
                name=application1.name,
                address=application1.address,
                reason_id=application1.reason.id,
                enable = True,
                # rebornreason_id=1,
                applyperson = application1.applyperson,
                industry = application1.industry,
                applytime = application1.applytime,
                level=application1.level,
                outerlevel = application1.outerlevel
            )
            application.objects.get(id=id).delete()

        messages.add_message(request, messages.SUCCESS, '审核通过'.format(len(ids)))

    test.short_description='通过'

    # 自 3.4+ 支持confirm确认提示
    test.confirm = '您确定要通过这些认定吗？' 
   
    def test1(self, request, queryset):
        ids = request.POST.getlist('_selected_action')
        for id in ids:
            application1 = application.objects.get(id=id)
            employe.objects.create(
                name=application1.name,
                address=application1.address,




                industry = application1.industry
            )
            application.objects.get(id=id).delete()

        messages.add_message(request, messages.SUCCESS, '审核拒绝'.format(len(ids)))

    test1.short_description='拒绝'

    # 自 3.4+ 支持confirm确认提示
    test1.confirm = '您确定要拒绝这些认定吗？' 
    actions=['test','test1']

@admin.register(defaultperson)
class default(ImportExportActionModelAdmin, AjaxAdmin):
    resource_class = ProxyResource
    list_display = ( 'name', 'industry', 'address','enable','outerlevel','reason','level','applyperson','applytime','rebornreason')
    search_fields = ('name', 'industry', 'address','reason','level','applyperson','rebornreason')
    raw_id_fields = ('reason','rebornreason')
    
    # search_fields = ('name')
    list_per_page = 20
    def test1(self, request, queryset):
        ids = request.POST.getlist('_selected_action')
        for id in ids:
            application1 = defaultperson.objects.get(id=id)
            reborn_application.objects.create(
                name=application1.name,
                address=application1.address,
                reason_id=application1.reason.id,
                enable = True,
                # rebornreason_id=1,
                applyperson = application1.applyperson,
                industry = application1.industry,
                applytime = application1.applytime,
                level=application1.level,
                outerlevel = application1.outerlevel
            )
            defaultperson.objects.get(id=id).delete()

        messages.add_message(request, messages.SUCCESS, '审核拒绝'.format(len(ids)))

    test1.short_description='拒绝'

    # 自 3.4+ 支持confirm确认提示
    test1.confirm = '您确定要拒绝这些认定吗？' 
   
    def test(self, request, queryset):
        ids = request.POST.getlist('_selected_action')
        for id in ids:
            application1 = defaultperson.objects.get(id=id)
            employe.objects.create(
                name=application1.name,
                address=application1.address,




                industry = application1.industry
            )
            defaultperson.objects.get(id=id).delete()

        messages.add_message(request, messages.SUCCESS, '审核通过'.format(len(ids)))

    test.short_description='通过'

    # 自 3.4+ 支持confirm确认提示
    test.confirm = '您确定要通过这些认定吗？' 
    actions=['test','test1']


