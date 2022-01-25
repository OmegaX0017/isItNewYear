from unicodedata import name
from django.urls import path

from hello.views import david, weslley

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("weslley", views.weslley, name="weslley"),
    path("david", views.david, name="david"),
]