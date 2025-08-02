from django.urls import path

from . import views

urlpatterns = [
    path("", views.members, name="members"),
    path("details/<int:id>", views.details, name="details"),
    path("add_member/", views.add_member, name="add_member"),
    path("update_member/<int:id>/", views.update_member, name="update_member"),
    path("delete_member/<int:id>/", views.delete_member, name="delete_member"),
]
