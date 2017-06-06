from django.db import models


class Note(models.Model):
	owner = models.ForeignKey('auth.User', related_name='note_owner', on_delete=models.CASCADE)
	title = models.CharField(max_length=100, blank=True)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

