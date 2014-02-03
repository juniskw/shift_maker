from django.db import models

#### Base ####
class Date(models.Model):

	date = models.DateField()

	def strfdate(self):
		return self.date.strftime('%Y/%m/%d,%a')

	class Meta:
		abstract = True	# This class is not make table

class TimeTable(models.Model):
	start = models.TimeField(default='00:00')
	end = models.TimeField(default='00:00')

	def unicode_timetable(self):
		timef = '%H:%M'
		start,end = self.start,self.end
		return "%s ~ %s" % ( start.strftime(timef),end.strftime(timef) )

	class Meta:
		abstract = True	# This class is not make table

#### Main ####
###### Staff ######
class WorkTime(TimeTable):
	title = models.CharField(max_length=50,unique=True)

	def __unicode__(self):
		return "%s (%s)" % ( self.title,self.unicode_timetable(), )

class StaffSchedule(Date):
	staff = models.ForeignKey('staff.Staff',unique_for_date='date')

	shift = models.ForeignKey(WorkTime)

	def __unicode__(self):
		return "[%s] %s => %s" % ( self.staff,self.strfdate(),self.shift, )

###### Guest ######
class GuestSchedule(Date,TimeTable):
	guest = models.ForeignKey('guest.Guest',unique_for_date='date')

	def __unicode__(self):
		return "[%s] %s (%s)" % ( self.guest,self.strfdate(),self.unicode_timetable(), )
