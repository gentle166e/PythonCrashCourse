#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/04/03 Friday 23:16:49
@Author     :Le
@LastEditor :
@EditTime   :
'''


from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

'''为应用程序users定以URL模式'''

app_name = 'users'

urlpatterns = [
    # 登录页面
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'),
        name='login'),
    # url(r'^login/$', views.login, name='login'),
    # 注册页面
    url(r'^register/$', views.register, name='register'),
    # 注销页面
    url(r'^logout/$', views.logout_view, name='logout'),
]
