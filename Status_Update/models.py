from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Manage(models.Model):
    date = models.DateTimeField()

    name = models.ForeignKey(
        User, related_name='task', on_delete=models.CASCADE)
    engineer = models.CharField(max_length=256, blank=True)
    year = models.IntegerField(blank=True)
    week = models.IntegerField(null=True)
    task = models.CharField(max_length=600, blank=True)
    comments = models.CharField(max_length=700, blank=True)
    status = models.CharField(max_length=256, blank=True)
    team = models.CharField(max_length=256, blank=True)

    class Meta:
        db_table = 'weekly_update'

    def __str__(self):
            # Built-in attribute of django.contrib.auth.models.User !
        return self.task
