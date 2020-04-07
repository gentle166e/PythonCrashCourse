from django.contrib import admin

# Register your models here.

from learn_logs.models import Topic, Entry

# 让Django通过管理网站管理我们的模型
admin.site.register(Topic)
admin.site.register(Entry)
