from django.db import models

class Schedule(models.Model):
	day = models.DateField()	# default?

	staff = models.ManyToManyField('staff.models.Staff')
	coming_guest = models.ManyToManyField('guest.models.ComingGuest')

	event = models.Field( choices=(	# models haven`t ChoiceField
		( 'Simple event:',models.CharField() ),
		( 'Big event:',models.OneToOneField('BigEvent') ),
	),blank=True )

	shift_requests = models.ManyToManyField('ShiftRequest',blank=True)

	def __unicode__(self):
		return self.day.strftime('%Y/%m/%d,%a')

class BigEvent(models.Model):
	event_title = models.CharField(max_length=50)

	date = models.ForeignKey('Schedule')

	start_time = models.TimeField()	# default?
	end_time = models.TimeField()	# default?

	staff = models.ManyToManyField('staff.models.Staff',blank=True)
	guest = models.ManyToManyField('guest.models.Guest',blank=True)

	def __unicode__(self):
		return event_title

class ShiftRequest(models.Model):
	staff = models.ForeignKey('staff.models.Staff')
	request = models.ManyToManyField('staff.models.WorkTime',blank=True,default="Off")

	def __unicode__(self):
		return "%s => %s" % (staff,request,)
