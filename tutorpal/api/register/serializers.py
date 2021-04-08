from .models import User, Student, Tutor, Review
from rest_framework import serializers
# from django.core.exceptions import ObjectDoesNotExist
# from typing import Union


class UserViewingSerializer(serializers.ModelSerializer):
    is_student = serializers.BooleanField(source='has_student', read_only=True)
    is_tutor = serializers.BooleanField(source='has_tutor', read_only=True)

    def has_student(self, user: User) -> bool:
        return user.has_student

    def has_tutor(self, user: User) -> bool:
        return user.has_tutor

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'profile_pic', 'is_student', 'is_tutor'
        ]


class UserOwnerSerializer(serializers.ModelSerializer):
    # is_student = serializers.SerializerMethodField('has_student')
    # is_tutor = serializers.SerializerMethodField('has_tutor')
    is_student = serializers.BooleanField(source='has_student', read_only=True)
    is_tutor = serializers.BooleanField(source='has_tutor', read_only=True)

    def has_student(self, user: User) -> bool:
        return user.has_student

    def has_tutor(self, user: User) -> bool:
        return user.has_tutor

    class Meta:
        model = User
        fields = [
            'id', 'email', 'is_student', 'is_tutor',
            'first_name', 'last_name', 'profile_pic', 'password',
            'student_pk', 'tutor_pk',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # print(validated_data)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()
        return user


class StudentOwnerSerializer(serializers.ModelSerializer):
    user = UserOwnerSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            'id', 'user', 'parent_email', 'birth_date'
        ]
        # depth = 1


class StudentViewingSerializer(serializers.ModelSerializer):
    user = UserViewingSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user']
        # depth = 1


class ReviewSerializer(serializers.ModelSerializer):
    student = StudentViewingSerializer(read_only=True)
    tutor = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 'tutor', 'student', 'stars', 'description'
        ]


class TutorOwnerSerializer(serializers.ModelSerializer):
    user = UserOwnerSerializer(read_only=True)

    average_reviews = serializers.FloatField(read_only=True)
    free_tutoring_given = serializers.DurationField(read_only=True)
    num_classes = serializers.IntegerField(read_only=True)
    num_reviews = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tutor
        fields = [
            'id', 'user', 'qualifications', 'what_you_teach',
            'subjects', 'birth_date', 'bio', 'rates', 'occupation', 'linkedIn',
            'verified', 'prof_exp', 'teach_exp', 'education', 'school', 'gpa', 'major',
            'gender', 'tutor_type', 'availability', 'average_reviews',
            'free_tutoring_given', 'paypal_email', 'num_classes', 'num_reviews'
        ]

    extra_kwargs = {
        # 'average_reviews': {'read_only': True, "required": False, 'allow_null': True},
        # 'free_tutoring_given': {'read_only': True, "required": False, 'allow_null': True},
        'linkedIn': {"required": False, 'allow_null': True}
    }


class TutorViewingSerializer(serializers.ModelSerializer):
    user = UserViewingSerializer(read_only=True)
    # reviews = serializers.SerializerMethodField('get_reviews')

    # def get_reviews(self, tutor):
    #     return ReviewSerializer(instance=Review.objects.filter(tutor=tutor)[:50], many=True).data

    class Meta:
        model = Tutor
        fields = [
            'id', 'user', 'qualifications', 'what_you_teach',
            'subjects', 'birth_date', 'bio', 'rates', 'occupation', 'linkedIn',
            'verified', 'prof_exp', 'teach_exp', 'education', 'school', 'gpa', 'major',
            'gender', 'tutor_type', 'availability', 'average_reviews', 'free_tutoring_given',  # 'reviews'
        ]
    extra_kwargs = {'verified': {'read_only': True}, 'average_reviews': {
        'read_only': True}, 'free_tutoring_given': {'read_only': True}}

    # def update(self, instance, validated_data):
    #     instance.qualifications = validated_data.get(
    #         'qualifications', instance.qualifications)
    #     instance.what_you_teach = validated_data.get(
    #         'what_you_teach', instance.what_you_teach)
    #     instance.subjects = validated_data.get('subjects', instance.subjects)
    #     instance.birth_date = validated_data.get(
    #         'birth_date', instance.birth_date)
    #     instance.bio = validated_data.get('bio', instance.bio)
    #     instance.rates = validated_data.get('rates', instance.rates)
    #     instance.occupation = validated_data.get(
    #         'occupation', instance.occupation)
    #     instance.linkedIn = validated_data.get('linkedIn', instance.linkedIn)
    #     instance.prof_exp = validated_data.get('prof_exp', instance.prof_exp)
    #     instance.teach_exp = validated_data.get(
    #         'teach_exp', instance.teach_exp)
    #     instance.education = validated_data.get(
    #         'education', instance.education)
    #     instance.school = validated_data.get('school', instance.school)
    #     instance.gpa = validated_data.get('gpa', instance.gpa)
    #     instance.major = validated_data.get('major', instance.major)
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.tutor_type = validated_data.get(
    #         'tutor_type', instance.tutor_type)
    #     instance.availability = validated_data.get(
    #         'availability', instance.availability)
    #     instance.save()
    #     return instance
