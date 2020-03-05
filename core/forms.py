from django import forms

from .models import Habit


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('name', 'description', 'goal_value', 'goal_unit', 'user')