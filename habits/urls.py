"""habits URL Configuration

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
from django.conf import settings
from django.urls import path, include
from core import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.habits, name = 'habits'),
    path('habits/<int:pk>', views.habit_detail, name = "habit-detail"),
    path('habits/edit/<int:pk>', views.edit_habit, name='edit-habit'),
    path('logs/edit/<int:pk>', views.edit_log, name='edit-log'),
    path('habits/delete/<int:pk>', views.delete_habit, name = 'delete-habit'),
    path('logs/delete/<int:pk>', views.delete_log, name = 'delete-log'),
    path('habits/new/', views.new_habit, name = 'new-habit'),
    path('habits/track/<int:pk>', views.track_habit, name = 'track-habit'),
    path('accounts/', include('registration.backends.default.urls'), name='login'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns