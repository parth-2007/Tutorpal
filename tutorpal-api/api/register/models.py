from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# import os
# from django.conf import settings
from PIL import Image
from datetime import timedelta
# from dry_rest_permissions.generics import authenticated_users


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    # is_tutor = models.BooleanField(default=False)
    # is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    timestamp = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(
        default='person.png', upload_to='profile_pics/')
    last_reset = models.DateTimeField(null=True, blank=True)
    student_pk = models.IntegerField(null=True, blank=True)
    tutor_pk = models.IntegerField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    @property
    def has_student(self):
        return self.student_pk is not None

    @property
    def has_tutor(self):
        return self.tutor_pk is not None

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_pic.path)

        if img.height > 128 or img.width > 128:
            output_size = (128, 128)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

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
        # return request.user.is_anonymous
        return False


# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent_email = models.EmailField()
    birth_date = models.DateField(help_text="YYYY-MM-DD")

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        return True

    def has_object_write_permission(self, request):
        return self.user == request.user

    @staticmethod
    # @authenticated_users
    def has_create_permission(request):
        return False
        # if hasattr(request.user, "student") or hasattr(request.user, "tutor"):
        #     return False
        # else:
        #     return True


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paypal_email = models.EmailField(blank=True)
    qualifications = models.TextField(max_length=1000)
    what_you_teach = models.TextField(
        max_length=1000, help_text="Give us a class description.")
    subjects = models.CharField(max_length=100)
    birth_date = models.DateField(help_text="YYYY-MM-DD")
    bio = models.TextField(
        max_length=1000, help_text="Tell potential students about yourself")
    rates = models.DecimalField(
        help_text="How much will you charge per hour?", max_digits=10, decimal_places=2)
    occupation = models.CharField(max_length=100)
    linkedIn = models.URLField(
        max_length=200, help_text="You may optionally put your LinkedIn profile URL.  Make sure to put it in the format of https://www.linkedin.com/in/[rest of url]", blank=True)
    verified = models.BooleanField(default=False)
    prof_exp = models.IntegerField()
    teach_exp = models.IntegerField()
    education = models.CharField(choices=(("High School", "High School"), ("Bachelors Degree",
                                                                           "Bachelors Degree"), ("Masters Degree", "Masters Degree"), ("Ph.D.", "Ph.D.")), max_length=16)
    school = models.CharField(blank=True, max_length=100)
    gpa = models.FloatField(blank=True, null=True)
    major = models.CharField(blank=True, max_length=50)
    gender = models.CharField(choices=(("Male", "Male"), ("Female", "Female"), (
        "Other", "Other"), ("Prefer Not To Say", "Prefer Not To Say")), max_length=17)
    tutor_type = models.CharField(max_length=50, blank=True)
    availability = models.CharField(
        max_length=500, help_text="Please explain your availability times.", blank=True)
    num_classes = models.IntegerField(default=0)
    average_reviews = models.FloatField(default=0.0)
    num_reviews = models.IntegerField(default=0)
    free_tutoring_given = models.DurationField(default=timedelta(hours=0))

    @property
    def rank(self):
        rank = self.average_reviews * 4 + self.num_reviews * 2 + self.num_classes
        return rank

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True

    @staticmethod
    def has_write_permission(request):
        return True

    def has_object_write_permission(self, request):
        return self.user == request.user

    @staticmethod
    # @authenticated_users
    def has_create_permission(request):
        return False
        # if hasattr(request.user, "student") or hasattr(request.user, "tutor"):
        #     return False
        # else:
        #     return True


class Review(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    stars = models.IntegerField(choices=[(0, "0 stars"), (1, "1 star"), (
        2, "2 stars"), (3, "3 stars"), (4, "4 stars"), (5, "5 stars")])
