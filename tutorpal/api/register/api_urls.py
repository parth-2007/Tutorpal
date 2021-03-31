from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api_views.users import UserList, UserDetail, student, tutor
from .api_views.tutors import TutorList, TutorDetail, user
from .api_views.students import StudentList, StudentDetail, user_
from .api_views.reviews import ReviewDetail, ReviewList

urlpatterns = [
    path('v1/users/', UserList.as_view()),
    path('v1/users/<pk>/', UserDetail.as_view()),
    path('v1/users/<pk>/student/', student),
    path('v1/users/<pk>/tutor/', tutor),

    path('v1/tutors/', TutorList.as_view()),
    path('v1/tutors/<pk>/', TutorDetail.as_view()),
    path('v1/tutors/<pk>/user/', user),

    path('v1/students/', StudentList.as_view()),
    path('v1/students/<pk>/', StudentDetail.as_view()),
    path('v1/students/<pk>/user/', user_),

    path('v1/reviews/', ReviewList.as_view()),
    path('v1/reviews/<int:pk>', ReviewDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
