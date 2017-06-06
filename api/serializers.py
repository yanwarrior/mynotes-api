from django.contrib.auth.models import User
from rest_framework import serializers
from notes.models import Note


class UserSerializer(serializers.ModelSerializer):
	note_owner = serializers.HyperlinkedRelatedField(many=True, view_name='api:note-detail', read_only=True)

	class Meta:
		model = User
		fields = ('id', 'note_owner', 'username', 'email')
		

class NoteSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Note
		fields = ('id', 'owner', 'title', 'content', 'created')