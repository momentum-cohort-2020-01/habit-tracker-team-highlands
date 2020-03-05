from django.shortcuts import render
from django.http import HttpResponse

from .models import Habit, Unit, Log


def habits(request):
    habits = Habit.objects.all()
    return render(request, 'core/habits.html', {'habits': habits})

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'core/habit_detail.html', {'habit': habit, "pk": pk})

# Create your views here.
