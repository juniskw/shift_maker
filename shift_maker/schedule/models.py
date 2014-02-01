from django.db import models

class Schedule(models.Model):
	day = models.DateField()	# default?

#	staff = models.ManyToManyField('staff.models.Staff')
#	coming_guest = models.ManyToManyField('guest.models.ComingGuest')

#	shift_requests = models.ManyToManyField('ShiftRequest',blank=True)

	def __unicode__(self):
		return self.day.strftime('%Y/%m/%d,%a')

class Event(models.Model):
	event_title = models.CharField(max_length=50)

	date = models.ForeignKey(Schedule)

	start_time = models.TimeField(blank=True)	# default?
	end_time = models.TimeField(blank=True)	# default?

	from staff.models import Staff
	staff = models.ManyToManyField(Staff,blank=True)
	from guest.models import Guest
	guest = models.ManyToManyField(Guest,blank=True)

	def __unicode__(self):
		return event_title

#class ShiftRequest(models.Model):
#	staff = models.ForeignKey('staff.models.Staff')
#	request = models.ManyToManyField('staff.models.WorkTime',blank=True,default="Off")

#	def __unicode__(self):
#		return "%s => %s" % (staff,request,)
