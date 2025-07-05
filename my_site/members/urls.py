from django.urls import path

from . import views

urlpatterns = [
    path("", views.members, name="members"),
    path("details/<int:id>", views.details, name="details"),
    path("add_member/", views.add_member, name="add_member"),
]
