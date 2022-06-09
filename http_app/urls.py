from django.urls import path
from .views import TestCaseView


urlpatterns = [
    path('test_case', TestCaseView.as_view())
]