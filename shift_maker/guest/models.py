from django.db import models

class Guest(models.Model):
	name = models.CharField(max_length=40)

	def __unicode__(self):
		return self.name
