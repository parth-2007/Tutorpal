from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from .models import User, Student, Tutor, Review
import random
import json
import os.path
from django.db.utils import IntegrityError

class UserTestCase(TestCase):
	def setUp(self):
		path = os.path.dirname(__file__)
		filename = os.path.join(path, 'names.json')
		names = json.loads(open(filename).read())
		for i in range(100):
			name = random.choice(names).lower()
			randbool = bool(random.getrandbits(1))
			try:
				User.objects.create(
					email=f"{name}@afdfdsf.ddfdfdf",
					first_name=name,
					last_name=random.choice(names),
					is_tutor=randbool,
					is_student=False,
				)
			except IntegrityError:
				User.objects.create(
					email=f"{name}@{name}ssdf.ddfddfdf",
					first_name=name,
					last_name=random.choice(names),
					is_tutor=randbool,
					is_student=False,
				)
		print('Created Users!')

	def testCase(self):
		factory = APIRequestFactory()
		get_user_list = factory.get('/users/')

