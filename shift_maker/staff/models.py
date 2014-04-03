from django.db import models
from django.contrib.auth.models import User
from owner.models import GroupSchedule


class Staff(models.Model):
	groupschedule = models.ForeignKey(GroupSchedule)

	name = models.CharField(max_length=40)

	user = models.OneToOneField(User,null=True,blank=True)

	class Meta:
		unique_together = ( ('name','groupschedule',), )

	def __unicode__(self):
		return self.name
