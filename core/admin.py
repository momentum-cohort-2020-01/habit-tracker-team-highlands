from django.contrib import admin

from .models import Habit, Unit, Log

admin.site.register(Habit)
admin.site.register(Unit)
admin.site.register(Log)

# Register your models here.
