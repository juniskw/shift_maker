from django.db import models

class WorkTime(models.Model):
	title = models.CharField(max_length=50)

	start_time = models.TimeField()
	end_time = models.TimeField()

#	staffs = models.ManyToManyField('Staff')
	
	def __unicode__(self):
		return self.title

class Staff(models.Model):
	name = models.CharField(max_length=40)

	worktimes = models.ManyToManyField(WorkTime)

	drive_skill = models.BooleanField()

	#shift = models.OneToOneField()

	def __unicode__(self):
		return self.name

class Shift(models.Model):

	work_time = models.ForeignKey(WorkTime)

	staff = models.OneToOneField(Staff)

	from schedule.models import Schedule
	date = models.ForeignKey(Schedule)

	def __unicode__(self):
		return "[%s]%s" % (self.work_time,self.date,)
