from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.exceptions import NotAuthenticated
from .authentication import BearerAuthentication
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer


class TestCaseView(APIView):

    throttle_classes = ([AnonRateThrottle,])
    authentication_classes = ([BearerAuthentication,])
    renderer_classes = [TemplateHTMLRenderer,]
    template_name = 'http_app/test_static_page.html'

    def get(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated
        return Response()



