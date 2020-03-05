from django import forms

from .models import Habit, Log, Unit


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('name', 'description', 'goal_value', 'goal_unit', 'user')

class ActivityForm(forms.ModelForm):

    class Meta:
        model = Log
        fields = ('activity_date', 'value','comments')