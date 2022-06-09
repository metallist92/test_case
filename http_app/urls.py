from django.urls import path
from .views import TestCaseView


urlpatterns = [
    path('', TestCaseView.as_view())
]