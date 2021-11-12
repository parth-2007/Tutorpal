import pytz

from django.utils import timezone


class timezonemiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.COOKIES.get('tz_name')
        if tzname and tzname in pytz.all_timezones:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)
