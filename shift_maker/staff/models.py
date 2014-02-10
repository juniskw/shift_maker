from django.db import models
from schedule.models import Date,TimeTable


class WorkTime(TimeTable):
	title = models.CharField(max_length=50,unique=True)

	def __unicode__(self):
		return "%s (%s)" % ( self.title,self.unicode_timetable(), )


class Staff(models.Model):
	name = models.CharField(max_length=40,unique=True)

	def __unicode__(self):
		return self.name


class StaffSchedule(Date):
	staff = models.ForeignKey(Staff,unique_for_date='date')

	shift = models.ForeignKey(WorkTime)

	def __unicode__(self):
		return "[%s] %s => %s" % ( self.staff,self.strfdate(),self.shift, )


class NgShift(Date):
	staff = models.ForeignKey(Staff,unique_for_date='date')

	ng_shift = models.ManyToManyField(WorkTime)

	def unicode_values(self):
		values = self.ng_shift.values_list('title')
		result = ""

		for value in values:
				  result += str(value[0]) + ","

		return result

	def __unicode__(self):
		return "[%s] NG => %s" % ( self.staff,self.unicode_values() )
