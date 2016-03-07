from __future__ import unicode_literals

from django.db import models
from django.conf import settings
# Create your models here.

class Contact(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	name = models.CharField(max_length=120, default='', blank=True)
	email = models.EmailField()
	subject = models.CharField(max_length=120)
	message = models.TextField()

	def __unicode__(self):
		if self.name:
			return self.name
		else:
			return self.email
