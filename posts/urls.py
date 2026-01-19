# posts/urls.py
from django.urls import path
from .views import (
    sticky_note_list,
    sticky_note_detail,
    sticky_note_create,
    sticky_note_update,
    sticky_note_delete,
    sticky_note_complete
    )

urlpatterns = [
    # URL pattern for displaying a list of all the sticky notes
    path("", sticky_note_list, name="sticky_note_list"),

    # URL pattern for displaying details of a specific sticky note
    path("post/<int:pk>/", sticky_note_detail, name="sticky_note_detail"),

    # URL pattern for creating a new sticky note
    path("post/new/", sticky_note_create, name="sticky_note_create"),

    # URL pattern for updating an existing sticky note
    path("post/<int:pk>/edit/", sticky_note_update, name="sticky_note_update"),

    # URL pattern for deleting an existing sticky note
    path("post/<int:pk>/delete/", sticky_note_delete,
         name="sticky_note_delete"),

    # URL pattern for marking an existing sticky note as complete
    path("post/<int:pk>/mark_complete/", sticky_note_complete,
         name="sticky_note_complete"),
]
