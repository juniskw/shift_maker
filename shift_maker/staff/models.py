from django.db import models
from schedule.models import Date,TimeTable#,MonthCalendar


class WorkTime(TimeTable):
	title = models.CharField(max_length=50,unique=True)

	#simbol = models.CharField(max_length=5,unique=True)

	def __unicode__(self):
		return self.title


class Staff(models.Model):
	name = models.CharField(max_length=40,unique=True)

	def __unicode__(self):
		return self.name


class StaffSchedule(Date):
	##monthcalendar = models.ForeignKey(MonthCalendar)

	staff = models.ForeignKey(Staff,unique_for_date='date')

	shift = models.ForeignKey(WorkTime)

	#leader = models.BooleanField(default=False)

	#phoner = models.BooleanField(default=False)

	def __unicode__(self):
		return self.strfdate()

class NgShift(Date):
	##monthcalendar = models.ForeignKey(MonthCalendar)

	staff = models.ForeignKey(Staff,unique_for_date='date')

	ng_shift = models.ManyToManyField(WorkTime)

	
	def ng_values(self):
		values = self.ng_shift.values_list('title')
		
		return ",".join( reduce( lambda x,y:x + y ,values ) )
	

	def __unicode__(self):
		return self.staff.name
