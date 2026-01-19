
# Register your models here.
from django.contrib import admin
from .models import StickyNote
from .models import Author


admin.site.register(StickyNote)
admin.site.register(Author)
