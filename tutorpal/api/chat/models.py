from register.models import User, Tutor, Student
from django.db import models
from django.utils import timezone
from dry_rest_permissions.generics import authenticated_users


class Room(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor_connected = models.BooleanField(default=False)
    student_connected = models.BooleanField(default=False)
    tutor_unread_msgs = models.IntegerField(default=0)
    student_unread_msgs = models.IntegerField(default=0)

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        if hasattr(request.user, 'tutor'):
            return self.tutor == request.user.tutor
        if hasattr(request.user, 'student'):
            return self.student == request.user.student

    @staticmethod
    def has_write_permission(request):
        return False

    def has_object_write_permission(self, request):
        return False

    @staticmethod
    @authenticated_users
    def has_create_permission(request):
        return True


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(
        Room, related_name="messages", on_delete=models.CASCADE)
    message = models.CharField(max_length=128)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)
    read = models.BooleanField(default=False)

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        return True

    def has_object_write_permission(self, request):
        return self == request.user

    @staticmethod
    def has_create_permission(request):
        return request.user.is_anonymous
