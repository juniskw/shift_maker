from django.db import models
from schedule.models import Date,TimeTable


class Guest(models.Model):
	name = models.CharField(max_length=40,unique=True)

	def __unicode__(self):
		return self.name


class GuestSchedule(Date,TimeTable):
	guest = models.ForeignKey(Guest,unique_for_date='date')

	def __unicode__(self):
		return self.strfdate()
