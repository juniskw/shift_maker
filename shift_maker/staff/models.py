from django.db import models
from schedule.models import Date,TimeTable


class WorkTime(TimeTable):
	title = models.CharField(max_length=50,unique=True)

	def __unicode__(self):
		return self.title


class Staff(models.Model):
	name = models.CharField(max_length=40,unique=True)

	def __unicode__(self):
		return self.name


class StaffSchedule(Date):
	staff = models.ForeignKey(Staff,unique_for_date='date')

	shift = models.ForeignKey(WorkTime)

	def __unicode__(self):
		return self.strfdate()

class NgShift(Date):
	staff = models.ForeignKey(Staff,unique_for_date='date')

	ng_shift = models.ManyToManyField(WorkTime)

	def unicode_values(self):
		values = self.ng_shift.values_list('title')

	  	result = ""

		for value in values:
				  result += str(value) + ","

		return result

	def __unicode__(self):
		return self.staff
