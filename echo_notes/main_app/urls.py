from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('notes/',views.all_notes, name='index'),
    path('notes/<int:note_id>/', views.notes_detail, name= "detail"),
    path('notes/create', views.CreateNote.as_view(), name ='note_form'),
    path('notes/<int:pk>/delete/', views.DeleteNote.as_view(), name = 'note_delete')


]

