from django.urls import path
from .views import NotesList, NotesDetail, home

urlpatterns = [
    path('', home),
    path('notes', NotesList.as_view()),
    path('<int:pk>/', NotesDetail.as_view()),
]
