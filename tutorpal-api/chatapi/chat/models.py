from os import defpath
from register.models import User, Tutor, Student
from django.db import models
from django.utils import timezone


class Room(models.Model):
    # id = models.IntegerField(primary_key=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_pk = models.IntegerField()
    tutor_pk = models.IntegerField()

    class Meta:
        managed = True


class Message(models.Model):
    # id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, related_name="messages", on_delete=models.CASCADE)
    message = models.CharField(max_length=128)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    tutor_read = models.BooleanField(default=False)
    student_read = models.BooleanField(default=False)
    
    class Meta:
        managed = True