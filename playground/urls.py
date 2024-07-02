from django.urls import path
from . import views


#urlconfirguation
urlpatterns = [
    path("hello/", views.say_hello, name="hello")
]