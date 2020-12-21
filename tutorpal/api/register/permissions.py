from rest_framework import permissions
from .models import Review

class IsOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.user == request.user

class CanMakeObj(permissions.BasePermission):
	# def has_object_permission(self, request, view, obj):
	# 	if request.method not in permissions.SAFE_METHODS and request.user.tutor is not None and request.user.student is not None:
	# 		return True
	# 	return False
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		elif hasattr(request.user, 'student') or hasattr(request.user, 'tutor'):
			return False
		else:
			return False

class CanMakeUser(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		elif request.user.is_authenticated:
			return False
		elif not request.user.is_authenticated:
			return True
		else:
			return False

class CanMakeReview(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		elif request.user.is_tutor:
			return False
		elif request.user.is_student:
			return True
		else:
			return False

class IsUserOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		elif request.user == obj:
			return True
		else:
			return False