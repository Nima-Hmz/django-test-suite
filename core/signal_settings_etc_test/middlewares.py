from django.conf import settings
from django.http import HttpResponse

class NimaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # code before the view and later middlewares
        if getattr(settings, 'MAINTAINANCE_MODE', False):
            return HttpResponse('site is under maintainance mode', status=503)
        
        # magic of the view and later middlewares
        response = self.get_response(request)

        # code after view

        return response