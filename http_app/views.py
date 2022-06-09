from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.exceptions import NotAuthenticated
from .authentication import BearerAuthentication


class TestCaseView(APIView):

    throttle_classes = ([AnonRateThrottle,])
    authentication_classes = ([BearerAuthentication,])

    def get(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated
        return Response(status=200, data={'authenticated_user': request.user.username})



