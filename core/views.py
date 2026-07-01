from django.shortcuts import render
from .models import Note


def index(request):
    notes = Note.objects.all()[:10]
    return render(request, 'core/index.html', {'notes': notes})
