#!/usr/bin/env python
# coding=utf-8


'''
@Description:
@Version    :0.1
@CreateTime :2020/04/02 Thursday 16:01:44
@Author     :Le
@LastEditor :
@EditTime   :
'''


from django.conf.urls import url

# .让python从当前的urls.py模块所在的文件夹中导入视图
from . import views


'''定义learn_logs的URL模式'''

app_name = 'learn_logs'

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),

    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 添加新主题的详细页面
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 添加新条目的详细页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # 编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
