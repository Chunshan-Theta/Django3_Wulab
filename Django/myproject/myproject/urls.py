"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))


"""
from django.conf.urls import include, url
from django.contrib import admin
from DemoProject.views import hello_world
from DemoProject.views import UsingStaticSource
from DemoProject.views import Http_From_Get
from DemoProject.views import Http_From_Post
from DemoProject.views import For_Cycle
from DemoProject.views import SQL_each
from DemoProject.views import SQL_all
from RestAPI.views import hello_world2
from RestAPI.views import ftidf_source
from RestAPI.views import ftidf_value
from RestAPI.views import jieba_cut
from RestAPI.views import textrank
from RestAPI.views import similarly_sentence
from phd_status.views import hello_world3
from phd_status.views import init_user
from phd_status.views import add_user
from phd_status.views import view_adduser
from phd_status.views import view_reviewRecords
from phd_status.views import del_records
from phd_status.views import edit_records
from phd_status.views import view_edit_records
from phd_status.views import view_reviewUsers
from phd_status.views import view_Login
from phd_status.views import login
urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^NewsTW/each/(?P<c>\S*)/$', SQL_each),
    url(r'^NewsTW/(?P<page>\S*)/$', SQL_all),
    url(r'^NewsTW/$', SQL_all,name="home"),
    url(r'^RestAPI/$', hello_world2,name="home2"),
    url(r'^RestAPI/ftidf/SourcData$', ftidf_source,name="FtidfSourcData"),
    url(r'^RestAPI/ftidf/$', ftidf_value,name="Ftidf"),
    url(r'^RestAPI/jieba/cut$', jieba_cut,name="JiebaCut"),
    url(r'^RestAPI/textrank$', textrank,name="textrank"),
    url(r'^RestAPI/similarly_sentence$', similarly_sentence,name="similarly_sentence"),
    url(r'^PHD/$', hello_world3),
    url(r'^PHD/initUser/$', init_user),
    url(r'^PHD/newUser/$', add_user),
    url(r'^PHD/login/$', login),
    url(r'^PHD/delrecords/$', del_records),
    url(r'^PHD/editrecords/$', edit_records),
    url(r'^PHD/view/adduser/$', view_adduser),
    url(r'^PHD/view/reviewRecords/$', view_reviewRecords),
    url(r'^PHD/view/editrecords/$', view_edit_records),
    url(r'^PHD/view/reviewUsers/$', view_reviewUsers),
    url(r'^PHD/view/Login/$', view_Login),
]
