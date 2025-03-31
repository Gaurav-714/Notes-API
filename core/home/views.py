from django.http import HttpResponse
from rest_framework import generics
from.models import Note
from .serializers import NoteSerializer


class NotesList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


def home(self, request):
    return HttpResponse("Hello World")