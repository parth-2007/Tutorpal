from rest_framework import permissions

class SessionPerm(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		return False
			
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		elif obj.student==request.user.student:
			return True
		elif obj.tutor==request.tutor and request.method in ("GET", "UPDATE"):
			return True
		else:
			return False
