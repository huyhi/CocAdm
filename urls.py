"""coc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from views.daily import DailyStatistic
from views.realtime import Realtime, PlayerRealtimeInf
from views.season import SeasonStatistics, Season
from views.testfile import TestView

urlpatterns = [
    path('api/', include([
        path('admin/', admin.site.urls),
        path('test/', TestView.as_view()),
        path(r'season/', Season.as_view()),
        path(r'season/<int:season_id>', SeasonStatistics.as_view()),
        path(r'daily/<str:player_tag>', DailyStatistic.as_view()),
        path(r'realtime/', Realtime.as_view()),
        path(r'realtime/<str:player_tag>', PlayerRealtimeInf.as_view()),
    ]))
]
