from django.test import TestCase
from django.urls import reverse
from .models import StickyNote

# Create your tests here.


# Arrange
class StickyNoteCreateViewTests(TestCase):
    def test_create_sticky_note(self):
        # Act
        response = self.client.post(
            reverse("sticky_note_create"),
            {
                "title": "Creating a Sticky Note",
                "content": "This is a test to determine the user"
                " experience",
                "is_pinned": True
            })

        # Assert
        new_sticky_note = StickyNote.objects.first()
        self.assertEqual(new_sticky_note.title, "Creating a Sticky Note")
        self.assertEqual(
            new_sticky_note.content, "This is a test to determine the user"
            " experience")

        self.assertEqual(StickyNote.objects.count(), 1)
        self.assertRedirects(
            response,
            reverse("sticky_note_list")
        )


# Arrange
class StickyNoteDeleteViewTests(TestCase):
    def test_delete_sticky_note(self):
        sticky_note = StickyNote.objects.create(
            title="Deleting this sticky note",
            content="Temporary note that is to be deleted"
        )

        # Act
        response = self.client.post(
            reverse("sticky_note_delete", args=[sticky_note.pk]))

        # Assert
        self.assertEqual(StickyNote.objects.count(), 0)
        self.assertRedirects(
            response,
            reverse("sticky_note_list")
        )


class StickyNoteDetailViewTests(TestCase):
    def test_detail_view_displays_note(self):
        # Arrange
        specific_note = StickyNote.objects.create(
            title="Detail View Note", content="Viewing this note")

        # Act
        response = self.client.get(
            reverse("sticky_note_detail", args=[specific_note.pk]))

        # Assert
        self.assertContains(response, "Detail View Note")
        self.assertEqual(response.status_code, 200)


class StickyNoteUpdateViewTests(TestCase):
    def test_update_sticky_note(self):
        # Arrange
        specific_note = StickyNote.objects.create(
            title="Old title and is to be updated",
            content="Old content and is to be updated")

        # Act
        response = self.client.post(
            reverse("sticky_note_update", args=[specific_note.pk]),
            {
                "title": "Updated title that has been updated", 
                "content": "Updated content that has been updated",
                "is_pinned": False}
            )

        # Assert
        specific_note.refresh_from_db()

        self.assertEqual(
            specific_note.title, "Updated title that has been updated")
        self.assertRedirects(response, reverse("sticky_note_list"))
