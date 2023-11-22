"""simpleui_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from article import views
from django.urls import path, include

admin.site.site_title = 'A3I HDU Backend Management System'
admin.site.site_header = 'A3I HDU'

urlpatterns = [ 
                #   path('admin',admin.site.urls),
                #   path('q/',include('hangye1.html')),
                  # 配置admindoc
path('api/', include('demo.urls')),
    re_path(r'doc/', include('django.contrib.admindocs.urls'), name='doc'),
    re_path(r'mdeditor/', include('mdeditor.urls')),
                  path('inde2/',include('article.urls1')),
                  path('inde/',views.quyu),
                  path('index2/',include('article.urls')),
                  path('index/',views.hangye),





              ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('', admin.site.urls),
]
