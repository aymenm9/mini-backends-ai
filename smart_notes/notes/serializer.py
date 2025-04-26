from rest_framework.serializers import ModelSerializer,ListField, CharField
from .models import Note, Tag



class TagSerializer(ModelSerializer):
    class Meta:
        model=Tag
        fields= '__all__'


class NoteSerializer(ModelSerializer):
    tags = ListField(
        child=CharField(),
        write_only=True
        )
    tags_obj = TagSerializer(
        source='tags',
        many=True,
        read_only=True
        )
    class Meta:
        model=Note
        fields='__all__'
        read_only_fields=['user']

    def create(self, validate_data):
        tags_data = validate_data.pop('tags')
        note = Note.objects.create(**validate_data)
        for tag in tags_data:
            new_tag = Tag.objects.get_or_create(name = tag)
            note.tags.add(new_tag)
