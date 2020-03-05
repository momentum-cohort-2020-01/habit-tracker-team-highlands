from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Habit, Log, User

from .forms import HabitForm, ActivityForm

@login_required
def habits(request):
    habits = Habit.objects.all()
    return render(request, 'core/habits.html', {'habits': habits})

def habit_detail(request, pk):
    habit = Habit.objects.get(pk=pk)
    habits = Habit.objects.all()
<<<<<<< HEAD
    logs = Log.objects.filter(habit=habit)
    return render(request, 'core/habit_detail.html', {'habit': habit, 'habits': habits, "pk": pk,'logs':logs})
=======
    return render(request, 'core/habit_detail.html', {'habit': habit, 'habits': habits, "pk": pk})
>>>>>>> ba23cc9... Create cards for all the habits on the homepage

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
<<<<<<< HEAD


def track_habit(request, pk):
    habits=Habit.objects.all()
    habit = get_object_or_404(Habit, pk=pk)
    log = Log(habit=habit)
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save()
            return redirect('habits')
    else:
        form = ActivityForm(instance=log)
    return render(request, 'core/track_habit.html', {'form': form, 'log': log, 'habits':habits})

def edit_log(request, pk):
    log = get_object_or_404(Log, pk=pk)
    habits = Habit.objects.all()
    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save()
            return redirect('habits')
    else:
        form = ActivityForm(instance=log)
    return render(request, 'core/edit_log.html', {'form': form, 'log': log, "habits" : habits})

def delete_log(request, pk):
    log = get_object_or_404(Log, pk=pk)
    log.delete()
    return redirect('/')
=======
>>>>>>> ba23cc9... Create cards for all the habits on the homepage

def error(request):
    habits = Habit.objects.all()
    return render(request, 'core/error.html', {'habits': habits})
