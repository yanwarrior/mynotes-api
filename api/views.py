from django.contrib.auth.models import User
from notes.models import Note
from .serializers import NoteSerializer, UserSerializer
from django.http import Http404
# from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	# agar url saat mengaskes adalah `user/usernamekamu/` 
	# dan bukan `user/1/` lagi. field lookup harus unik atau juga sebagai id.
	lookup_field = 'username'


class NoteList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = Note.objects.all()
	serializer_class = NoteSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def get_queryset(self):
		"""
		Filter data dengan query param.
		"""
		queryset = Note.objects.all()
		title = self.request.query_params.get('title')
		username = self.request.query_params.get('username')

		if title:
			queryset = Note.objects.filter(title__contains=title)

		if username:
			owner = User.objects.get(username=username)
			queryset = queryset.filter(owner=owner)

		return queryset


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
	queryset = Note.objects.all()
	serializer_class = NoteSerializer


