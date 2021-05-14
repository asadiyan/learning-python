from django.contrib import admin
from django.urls import path
from myapp import views

# "myapp" we pass this name in index.html file
# in the url section so jango comes here for detail named view
# it means we have name space here "myapp"
app_name = "myapp"

urlpatterns = [
    path("", views.index, name="index"),
    # here we use the id that we passed it in views
    # then because it is a intiger value
    # we covert it like this
    path("book/<int:book_id>/", views.detail, name="detail"),
]
