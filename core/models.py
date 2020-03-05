from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
#Pillow later perhaps?
Units = (
    ('Times', 'Times'),
    ('Seconds', 'Seconds'),
    ('Minutes', 'Minutes'),
    ('Hours', 'Hours'),
    ('Units', 'Units'),
    ('Steps', 'Steps')
)

class Habit(models.Model):
    name = models.CharField(max_length=100)
    goal_value = models.IntegerField(default=0)
    goal_unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    description = models.TextField(max_length=None)
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(to=User, related_name="users_habits", on_delete=models.CASCADE)
    
    

    def __str__(self):
        return f'Habit Name: {self.name} Daily goal for {self.user}: {self.description}'
    
    class Meta:
        ordering = ['-created_at']

    @property
    def get_days_tracked(self):
        return len(self.habit_log.all())
    

class Unit(models.Model):
    name = models.CharField(max_length=100, choices=Units)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Log(models.Model):
    created_at = models.DateField(auto_now=True)
    habit = models.ForeignKey(to=Habit, related_name="habit_log", on_delete=models.DO_NOTHING)  ##Might need null=true and blank=true here.
    value = models.IntegerField(default=0)
    comments = models.TextField(max_length=None)
    
    def __str__(self):
        return f'Date Tracked: {self.created_at}, Habit: {self.habit.pk}'

