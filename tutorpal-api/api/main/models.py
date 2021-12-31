from django.db import models
from register.models import User

# Create your models here.
class Feedback(models.Model):
    text = models.TextField(max_length=1024)

    def __str__(self) -> str:
        return f'{self.id} {self.text}'

class Bugs(models.Model):
    bug = models.TextField(max_length=1024)
    level = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.id} {self.level} {self.bug}'
