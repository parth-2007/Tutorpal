from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from datetime import timedelta


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
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        managed = True


# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parent_email = models.EmailField()
    birth_date = models.DateField(help_text="YYYY-MM-DD")

    class Meta:
        managed = True



class Tutor(models.Model):
    id = models.IntegerField(primary_key=True)
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

    class Meta:
        managed = True
