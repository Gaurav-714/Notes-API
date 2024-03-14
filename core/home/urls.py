from django.urls import path
from .views import NotesList, NotesDetail

urlpatterns = [
    path('', NotesList.as_view()),
    path('<int:pk>/', NotesDetail.as_view()),
]
