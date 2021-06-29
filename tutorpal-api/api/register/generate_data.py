import json
import os
import random
from datetime import datetime, timedelta
from session.models import Session
from .models import Review, Student, Tutor, User


# generates users along with tutors and students
# input is amount of iterations
def generate_users(iterations):
    names_dir = os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))) + "/register/names.json"
    names_json = open(names_dir)
    names = json.load(names_json)

    for _ in range(iterations):
        first_name = random.choice(names)
        last_name = random.choice(names)
        user = User.objects.create(
            email=first_name + last_name + "@example.com",
            first_name=first_name,
            last_name=last_name,
            is_active=True,
        )
        user.save()
        if random.randint(1, 2) == 1:
            tutor = Tutor.objects.create(
                qualifications="none",
                what_you_teach="something",
                subjects="nunya beezwax",
                birth_date=datetime.now(),
                bio="no",
                rates=15,
                occupation="nunya beezwax",
                prof_exp=42,
                teach_exp=69,
                education="nunya beezwax",
                school="nunya beezwax",
                gpa=3,
                major="nunya beezwax",
                gender="Other",
                tutor_type="idk",
                availability="when ur busy",
                user=user
            )
            tutor.save()
            user.tutor_pk = tutor.id
            user.save()
        else:
            student = Student.objects.create(
                parent_email="nunya@beezwax.baf",
                birth_date=datetime.now(),
                user=user
            )
            student.save()
            user.student_pk = student.id
            user.save()

    print('successfully generated users')


def generate_reviews(iterations):
    student_count = Student.objects.count()
    student = Student.objects.all()[random.randint(0, student_count - 1)]
    tutor_count = Tutor.objects.count()
    tutor = Tutor.objects.all()[random.randint(0, tutor_count - 1)]
    for _ in range(iterations):
        Review.objects.create(
            tutor=tutor,
            student=student,
            description="Generated review " * random.randint(1, 20),
            stars=random.randint(1, 5)
        )
    print("success")


def generate_sessions(iterations):
    for _ in range(iterations):
        student_count = Student.objects.count()
        student = Student.objects.all()[random.randint(0, student_count - 1)]
        tutor_count = Tutor.objects.count()
        tutor = Tutor.objects.all()[random.randint(0, tutor_count - 1)]
        free = bool(random.randint(0, 1))
        accepted = bool(random.randint(0, 1))
        call_url = ''.join(random.choice(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(30))
        started = bool(random.randint(0, 1))
        finished = bool(random.randint(0, 1)) if started else False
        # refunded = bool(random.randint(0, 1))
        Session.objects.create(
            student=student,
            tutor=tutor,
            date=datetime.now().date(),
            time_start=datetime.now().time(),
            time_end=datetime.now().time(),
            duration=timedelta(hours=1),
            price=0 if free else 69.42,
            free=free,
            description="a genrated class",
            call_url=call_url,
            accepted=accepted,
            rejected=False if accepted else True,
            canceled=bool(random.randint(0, 1)),
            started=started,
            finished=finished,
            # accessable=bool(random.randint(0, 1)),
            student_paid=started,
            tutor_paid=finished,
            # refund_requested=refunded,
            # refund_available=bool(random.randint(0, 1)),
            # refunded=refunded,
            tutor_emailed=started,
            student_emailed=started,
            parent_emailed=started,
            tutor_pk=tutor.pk,
            student_pk=student.pk
        )
    print("success!")
