from django.db import models
from schedule.models import Date,TimeTable
from owner.models import GroupSchedule


class Guest(models.Model):
	groupschedule = models.ForeignKey(GroupSchedule)

	name = models.CharField(max_length=40)

	class Meta:
		unique_together = ( ('name','groupschedule',), )

	def __unicode__(self):
		return self.name


class GuestSchedule(Date,TimeTable):
	guest = models.ForeignKey(Guest,unique_for_date='date')

	def __unicode__(self):
		return self.strfdate()
