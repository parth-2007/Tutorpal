from django.contrib import auth
from django.contrib.auth.models import User
from django.middleware.csrf import CsrfViewMiddleware
from django.utils.translation import ugettext_lazy as _
from rest_framework import authentication, exceptions


class CSRFCheck(CsrfViewMiddleware):
    def _reject(self, request, reason):
        # Return the failure reason instead of an HttpResponse
        return reason


class DRFSessionAuthentication(authentication.BaseAuthentication):
    # 'Session authentication against username/password for DRF'

    def authenticate(self, request):
        '''
        Returns a User if a correct username and password have been supplied
        using Django Session Authentication. Otherwise returns None.
        '''

        username = request.data.get('username')
        password = request.data.get('password')

        return self.authenticate_credentials(username, password, request)

    def authenticate_credentials(self, userid, password, request=None):
        '''
        Authenticate the userid and password against username and password
        with optional request for context.
        '''

        credentials = {
            auth.get_user_model().USERNAME_FIELD: userid,
            'password': password
        }
        user = auth.authenticate(request=request, **credentials)

        if user is None:
            raise exceptions.AuthenticationFailed(
                _('Invalid username/password.')
            )

        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                _('User inactive or deleted.')
            )

        self.enforce_csrf(request)

        return (user, None)

    def authenticate_header(self, request):
        return 'Session'

    def enforce_csrf(self, request):
        # 'Enforce CSRF validation for session based authentication.'

        reason = CSRFCheck().process_view(request, None, (), {})
        if reason:
            # CSRF failed, bail with explicit error message
            raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)
