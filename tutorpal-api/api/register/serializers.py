from .models import User, Student, Tutor, Review
from rest_framework import serializers
# from django.db.models import Count, Q
# from chat.models import Message  # remove
# from typing import Dict, Any
# from django.conf import settings


# class FastUserOwnerSerializer:
#     def __init__(self, user: User, *args, **kwargs):
#         print()
#         self.data = {
#             'id': user.id,
#             'email': user.email,
#             'is_student': user.has_student,
#             'is_tutor': user.has_tutor,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#             'profile_pic': settings.SITE_DOMAIN + settings.MEDIA_URL + str(user.profile_pic),
#             'student_pk': user.student_pk,
#             'tutor_pk': user.tutor_pk
#         }

#     class Meta:
#         model = User


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
        read_only_fields = fields


class UserOwnerSerializer(serializers.ModelSerializer):
    # is_student = serializers.SerializerMethodField('has_student')
    # is_tutor = serializers.SerializerMethodField('has_tutor')
    is_student = serializers.BooleanField(source='has_student', read_only=True)
    is_tutor = serializers.BooleanField(source='has_tutor', read_only=True)
    # unread = serializers.SerializerMethodField()  # and this

    def has_student(self, user: User) -> bool:
        return user.has_student

    def has_tutor(self, user: User) -> bool:
        return user.has_tutor

    # delete all
    # def get_unread(self, user: User) -> int:
    #     if user.has_tutor:
    #         unread_count = Message.objects.filter(room__tutor_pk=user.tutor_pk).exclude(author=user).aggregate(
    #             unread=Count('pk', filter=Q(tutor_read=False))
    #         )
    #         return unread_count.get('unread')
    #     elif user.has_student:
    #         unread_count = Message.objects.filter(room__student_pk=user.student_pk).exclude(author=user).aggregate(
    #             unread=Count('pk', filter=Q(student_read=False))
    #         )
    #         return unread_count.get('unread')

    class Meta:
        model = User
        fields = [
            'id', 'email', 'is_student', 'is_tutor',
            'first_name', 'last_name', 'profile_pic', 'password',
            'student_pk', 'tutor_pk',  # 'unread'  # and this
        ]
        extra_kwargs = {'password': {'write_only': True}, 'student_pk': {
            'read_only': True}, 'tutor_pk': {'read_only': True}}

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


class StudentViewingSerializer(serializers.ModelSerializer):
    user = UserViewingSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user']
        read_only_fields = fields


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
        'linkedIn': {"required": False, 'allow_null': True},
        'user': {'write_only': True}
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
            'subjects', 'bio', 'rates', 'occupation', 'linkedIn',
            'verified', 'prof_exp', 'teach_exp', 'education', 'school', 'gpa', 'major',
            'gender', 'tutor_type', 'availability', 'average_reviews', 'free_tutoring_given',  # 'reviews'
        ]
        read_only_fields = fields
    extra_kwargs = {'verified': {'read_only': True}, 'average_reviews': {
        'read_only': True}, 'free_tutoring_given': {'read_only': True}}


class NestedTutorSerializer(serializers.ModelSerializer):
    user = UserViewingSerializer(read_only=True)

    class Meta:
        model = Tutor
        fields = [
            'id', 'user', 'verified'
        ]
        read_only_fields = fields
