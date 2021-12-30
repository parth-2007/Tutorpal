from django.db import models
from register.models import User

# Create your models here.
class Feedback(models.Model):
    text = models.TextField(max_length=1024)

class Bugs(models.Model):
    bug = models.TextField(max_length=1024)
    level = models.IntegerField()
