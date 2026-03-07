from django.shortcuts import render, redirect
from .models import Note
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid Sign Up, Try again later..."
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

@login_required
def all_notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/index.html', {'notes': notes})

@login_required
def notes_detail(request, note_id):
    note = Note.objects.get(id= note_id)
    return render(request, 'notes/detail.html', {'note':note})

class CreateNote(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'note_text']

    def form_valid(self, form):
        form.instance.user =self.request.user
        return super().form_valid(form)

class UpdateNote(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'note_text']

class DeleteNote(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = '/notes/'




