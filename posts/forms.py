# posts/forms.py
from django import forms
from .models import StickyNote


class StickyNoteForm(forms.ModelForm):
    """Form for creating and updating Sticky Note objects.

    Fields:
    - title: CharField for the sticky note title.
    - content: TextField for the sticky note content.

    Meta class:
    - Defines the model to use (Stciky Note) and the fields
      to include in the form.

    :param form.ModelForm: Django's ModelForm class.
    """

    class Meta:
        model = StickyNote
        fields = ["title", "content", "author"]
