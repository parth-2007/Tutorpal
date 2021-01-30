from django.urls import path, re_path
from .views import auth
from django.conf.urls.static import static
from django.views.static import serve
import os

urlpatterns = [
    path('frontend/auth/', auth),
    # path('frontend/<str:dir>/<str:file>', godir)
]

urlpatterns += [
    # static('/frontend/',
    #        document_root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    re_path(r'^frontend/(?P<path>.*)$', serve,
            {'document_root': os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/frontend/templates/frontend'}),
]
