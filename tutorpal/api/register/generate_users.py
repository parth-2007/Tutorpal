import json
import random
from .models import Student, Tutor, User, Review
import os
from datetime import datetime


def generate_users():
    names_dir = os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))) + "/register/names.json"
    names_json = open(names_dir)
    names = json.load(names_json)

    print(names[3:9])

    for i in range(10):
        user = User.objects.create(
            first_name=random.choice(names),
            last_name=random.choice(names),
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
            )
            tutor.save(user=user)
        else:
            student = Student.objects.create(
                parent_email="nunya@beezwax.baf",
                birth_date=datetime.now()
            )
            student.save(user=user)
