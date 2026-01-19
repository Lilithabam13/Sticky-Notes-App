from django.shortcuts import render, get_object_or_404, redirect
from .models import StickyNote
from .forms import StickyNoteForm

# Create your views here.


def sticky_note_list(request):
    """View to display a list of all sticky notes.

    :param request: HTTP request object.
    :return: Rendered template with a list of sticky notes.
    """
    # Retrieve all sticky notes. Pinned first followed by newest
    sticky_notes = StickyNote.objects.all().order_by(
        "-is_pinned", "-created_at")

    # Creating a context dictionary to pass data
    context = {
        "sticky_notes": sticky_notes,
        "page_title": "List of Sticky Notes",
    }
    # Render template with list of all sticky notes
    return render(request, "posts/sticky_note_list.html", context)


def sticky_note_detail(request, pk):
    """View to display details of a specific sticky note.

    :param request: HTTP request object.
    :param pk: Primary key of the sticky note.
    :return: Rendered template with details of the specified sticky note.
    """
    # Retrieve specific sticky note or return 404 error if not found
    sticky_note = get_object_or_404(StickyNote, pk=pk)
    # Render template to display sticky note details
    return render(
        request, "posts/sticky_note_detail.html",
        {"sticky_note": sticky_note})


def sticky_note_create(request):
    """View to create a new sticky note.

    :param request: HTTP request object.
    :return: Rendered template for creating a new sticky note.
    """
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            # Creates sticky note instance without persistence
            sticky_note = form.save(commit=False)
            sticky_note.save()  # Ensure persistence
            return redirect("sticky_note_list")  # Redirect only if successful
    else:
        # GET request, creating an empty form
        form = StickyNoteForm()
        # Render form template for creating and send page to user
    return render(
        request, "posts/sticky_note_form.html", {"form": form})


def sticky_note_update(request, pk):
    """View to update an existing sticky note.

    :param request: HTTP request object.
    :param pk: Primary key of the sticky note to be updated.
    :return: Rendered template for updating the specified sticky note.
    """
    # Retrieve specific sticky note
    sticky_note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        # Bind submitted POST data with existing sticky note data
        form = StickyNoteForm(request.POST, instance=sticky_note)
        if form.is_valid():
            sticky_note = form.save(commit=False)
            sticky_note.save()
            return redirect("sticky_note_list")
    else:
        # GET request, pre filled form with current data
        form = StickyNoteForm(instance=sticky_note)
        # Render form template for editing
    return render(
        request, "posts/sticky_note_form.html", {"form": form})


def sticky_note_delete(request, pk):
    """View to delete an existing sticky note.

    :param request: HTTP request object.
    :param pk: Primary key of the sticky note to be deleted.
    :return: Redirect to the sticky_notes list after deletion.
    """
    sticky_note = get_object_or_404(StickyNote, pk=pk)
    if request.method == "POST":
        # Post user deletion, deletes sticky note from database
        sticky_note.delete()
        return redirect("sticky_note_list")
    # GET request, render confirmation page before deletion
    return render(
        request, "posts/sticky_note_confirm_delete.html",
        {"sticky_note": sticky_note})


def sticky_note_complete(request, pk):
    """View to mark an existing sticky note as completed.

    :param request: HTTP request object.
    :param pk: Primary key of the sticky note to be deleted.
    :return: Redirect to the sticky_notes list after completion marking
    """
    sticky_note = get_object_or_404(StickyNote, pk=pk)
    # Mark sticky note as complete using model method
    sticky_note.mark_complete()
    return redirect("sticky_note_list")
