from django.db import models

#### Base ####
class Date(models.Model):

	date = models.DateField()

	class Meta:
		abstract = True	# This class is not make table

class TimeTable(models.Model):
	start = models.TimeField(default='00:00')	# blank=True is?	# blank is Stayng or NightWork?
	end = models.TimeField(default='00:00')	# blank=True is?	# blank is Staying or NightWork?

	class Meta:
		abstract = True	# This class is not make table

#### Main ####
###### Staff ######
class WorkTime(TimeTable):
	title = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title

class DateAndStaff(Date):
	staff = models.ForeignKey('staff.Staff')

	def __unicode__(self):
		return "[%s] %s " % (self.staff,self.date.strftime('%Y/%m/%d,%a'),)

class StaffShift(models.Model):
	date_and_staff = models.OneToOneField( DateAndStaff )

	shift = models.ForeignKey(WorkTime)

	def __unicode__(self):
		return "%s => %s" % ( self.date_and_staff,self.shift )

###### Guest ######
class DateAndGuest(Date):
	guest = models.ForeignKey('guest.Guest')

	def __unicode__(self):
		return "[%s] %s " % (self.guest,self.date.strftime('%Y/%m/%d,%a'),)

class GuestPlan(TimeTable):
	date_and_guest = models.OneToOneField( DateAndGuest )

	def __unicode__(self):
		return "%s < %s > ~ < %s >" % ( self.date_and_guest,self.start,self.end )
