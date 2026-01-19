# posts/models.py
from django.db import models
from django.utils import timezone

# Create your models here.


class StickyNote(models.Model):
    """Model representing a sticky note.

    Fields:
    - title: CharField for the sticky note title with a maximum
      length of 255 characters.
    - content: TextField for the sticky note content.
    - created_at: DateTimeField set to the current date and time
      when the sticky note is created.
    - completed_at: DateTimeField set to the current date and time
      when the sticky note is completed.
    - is_pinned: BooleanField for the sorting of sticky notes in
      terms of priority.

    Relationships:
    - author: ForeignKey representing the author of the sticky note.

    Methods:
    - __str__: Returns a string representation of the sticky note,
     showing the title.

    :param models.Model: Django's base model class.
    """

    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_pinned = models.BooleanField(default=False)

    class Meta:
        # Ensures pinned sticky notes come first, followed
        # by the newest sticky notes.
        ordering = ["-is_pinned", "-created_at"]

    def mark_complete(self):
        if self.completed_at is None:
            self.completed_at = timezone.now()
            self.is_pinned = False  # completing a sticky note unpins it
            self.save()

    # Define a ForeignKey for the author's relationship
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    """Model representing the author of a sticky note.

    Fields:
    - name: CharField for the author's name.

    Methods:
    - __str__: Returns a string representation of the author,
      sharing the name.

    :param models.Model: Django's base model class.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
