# -*- coding:utf-8 -*-
# PROJECT_NAME : flapmmo
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com

from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('web.game.views',
                       url(r'^$', 'index_view', name='index'),
                       )
