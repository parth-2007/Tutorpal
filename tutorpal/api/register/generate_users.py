import json
import random
from .models import Student, Tutor, User, Review
import os


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
                # paypal_email
                # qualifications
                # what_you_teach
                # subjects
                # birth_date
                # bio
                # rates
                # occupation
                # linkedIn
                # verified
                # prof_exp
                # teach_exp
                # education
                # school
                # gpa
                # major
                # gender
                # tutor_type
                # availability
                # num_classes
                # average_reviews
                # num_reviews
                # free_tutoring_given
            )
