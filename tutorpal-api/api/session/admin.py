from django.contrib import admin
from .models import Session, Seminar, StudentSeminar

# Register your models here.
admin.site.register(Session)
admin.site.register(Seminar)
admin.site.register(StudentSeminar)
