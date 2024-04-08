from django.urls import path
from . import views

urlpatterns =[
    # When someone run the default path to this hello application, 
    # run the index function in the view file
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david"),
    path("<str:name>", views.greet, name="greet")
]