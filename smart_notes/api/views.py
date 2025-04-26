from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from notes.models import Note, Tag
from notes.serializer import NoteSerializer, TagSerializer
from .gen import generate
# Create your views here.



class NoteViewSet(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        note = serializer.validated_data
        summary = generate(note)
        serializer(summary=summary,user=self.request.user)


class NoteVeiwDetials(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    lookup_field='id'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)