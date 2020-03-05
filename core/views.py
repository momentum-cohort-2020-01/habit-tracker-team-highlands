from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Habit, Unit, Log

from .forms import HabitForm


def habits(request):
    habits = Habit.objects.all()
    return render(request, 'core/habits.html', {'habits': habits})

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    return render(request, 'core/habit_detail.html', {'habit': habit, "pk": pk})

def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save()
            form.save()
            return redirect('habits')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'core/edit_habit.html', {'form': form})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('/')

# Create your views here.
