from django.db import models

class Guest(models.Model):
	name = models.CharField(max_length=40)

	def __unicode__(self):
		return self.name

class GuestComing(models.Model):
	guest = models.ForeignKey(Guest)

	from schedule.models import Schedule
	date = models.ForeignKey(Schedule)	#

	come_time = models.TimeField()
	back_time = models.TimeField()

	def __unicode__(self):
		return "[%s] (%s), <%s> ~ <%s>" % ( self.guest,self.date,self.come_time.strftime('%H:%S'),self.back_time('%H:%S'), )
