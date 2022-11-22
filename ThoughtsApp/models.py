from django.contrib.auth.models import User
from django.contrib import admin
from django.db import models


class Thoughts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thought_text = models.CharField(max_length=3000)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
    )
    def __str__(self):
        return self.thought_text
