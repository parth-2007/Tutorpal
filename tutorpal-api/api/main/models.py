from django.db import models
from register.models import User

# Create your models here.
class Feedback(models.Model):
    text = models.TextField(max_length=1000)

class Bugs(models.Model):
    bug = models.TextField(max_length=1000)
    level = models.IntegerField(help_text="On a scale from 1-10, 1 being very important and 10 being small")
