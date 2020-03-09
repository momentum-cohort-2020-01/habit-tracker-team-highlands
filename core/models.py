import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
#Pillow later perhaps?

class Habit(models.Model):
    import datetime
    name = models.CharField(max_length=100)
    goal_value = models.IntegerField(default=0)
    goal_unit = models.CharField(max_length=100)
    description = models.TextField(max_length=None)
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(to=User, related_name="users_habits", on_delete=models.CASCADE)
    
    

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['-created_at']

    @property
    def get_days_tracked(self):
        return len(self.habit_log.all())  
    

class Log(models.Model):
    activity_date = models.DateField(default=datetime.date.today)
    habit = models.ForeignKey(to=Habit, related_name="habit_log", on_delete=models.DO_NOTHING)  ##Might need null=true and blank=true here.
    log_value = models.IntegerField(default=0)
    comments = models.TextField(max_length=None)
    
    def __str__(self):
        return f'Date Tracked: {self.activity_date}, Habit: {self.habit.pk}'

    class Meta:
         unique_together = ('habit', 'activity_date')