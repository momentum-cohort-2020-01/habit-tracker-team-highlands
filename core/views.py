from django.shortcuts import render
from django.http import HttpResponse

from .models import Habit, Unit, Log


def habits(request):
    habits = Habit.objects.all()
    return render(request, 'core/habits.html', {'habits': habits})

# Create your views here.
