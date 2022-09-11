from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as v

router = DefaultRouter()
router.register(r'sessions', v.SessionViewSet)
router.register(r'seminars', v.SeminarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('capture_order/<int:id>/', v.api_capture_order),
    path('finish_session/<int:id>/', v.finish_session),
    # path('test_payout/', v.test_payout)
]
