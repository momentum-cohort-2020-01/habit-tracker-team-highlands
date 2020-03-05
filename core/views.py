from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Habit, Unit, Log

from .forms import HabitForm


def habits(request):
    habits = Habit.objects.all()
    return render(request, 'core/habits.html', {'habits': habits})

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    habits = Habit.objects.all()
    return render(request, 'core/habit_detail.html', {'habit': habit, 'habits': habits, "pk": pk})

def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habits = Habit.objects.all()
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save()
            form.save()
            return redirect('habits')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'core/edit_habit.html', {'form': form, "habits" : habits})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('/')

def new_habit(request):
    habits = Habit.objects.all()
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect('habits')
    else:
        form = HabitForm()

    return render(request, 'core/new_habit.html', {'form': form, 'habits': habits})

# Create your views here.
