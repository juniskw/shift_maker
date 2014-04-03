from django.db import models
from owner.models import GroupSchedule


class Guest(models.Model):
	groupschedule = models.ForeignKey(GroupSchedule)

	name = models.CharField(max_length=40)

	class Meta:
		unique_together = ( ('name','groupschedule',), )

	def __unicode__(self):
		return self.name
