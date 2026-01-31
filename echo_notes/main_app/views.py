from django.shortcuts import render
from .models import Note
from django.views.generic.edit import CreateView, UpdateView , DeleteView

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def all_notes(request):
    notes = Note.objects.filter()
    return render(request, 'notes/index.html', {'notes': notes})

def notes_detail(request, note_id):
    note = Note.objects.get(id= note_id)
    return render(request, 'notes/detail.html', {'note':note})

class CreateNote(CreateView):
    model = Note
    fields = ['title', 'note_text']

class DeleteNote(DeleteView):
    model = Note
    success_url = '/notes/'
