from django.db import models
from register.models import Tutor, Student
from dry_rest_permissions.generics import authenticated_users

# Create your models here.


class Session(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    date = models.DateField(help_text="YYYY-MM-DD")
    time_start = models.TimeField()
    time_end = models.TimeField()
    duration = models.DurationField(blank=True)

    price = models.DecimalField(
        blank=True, max_digits=10, decimal_places=2, default=0)
    free = models.BooleanField(default=False)
    description = models.TextField(max_length=500, blank=True)
    subjects = models.CharField(max_length=64, blank=True)

    call_url = models.CharField(max_length=30, blank=True)

    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)

    started = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    accessable = models.BooleanField(default=False)

    student_paid = models.BooleanField(default=False)
    tutor_paid = models.BooleanField(default=False)

    # refund_requested = models.BooleanField(default=False)
    # refund_available = models.BooleanField(default=False)
    # refunded = models.BooleanField(default=False)
    # refund_description = models.TextField(blank=True)

    # tutor_emailed = models.BooleanField(default=False)
    # student_emailed = models.BooleanField(default=False)
    # parent_emailed = models.BooleanField(default=False)

    student_pk = models.IntegerField()
    tutor_pk = models.IntegerField()

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    @authenticated_users
    def has_write_permission(request):
        return request.user.is_authenticated

    @authenticated_users
    def has_object_write_permission(self, request):
        if request.user.has_tutor:
            return self.tutor_pk == request.user.tutor_pk
        elif request.user.has_student:
            return self.student_pk == request.user.student_pk
        else:
            return False

    @staticmethod
    @authenticated_users
    def has_create_permission(request):
        return request.user.has_student
