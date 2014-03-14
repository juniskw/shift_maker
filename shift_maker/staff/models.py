from django.db import models
from django.contrib.auth.models import User#,Group
from schedule.models import Date,TimeTable,MonthSchedule


class WorkTime(TimeTable):
	title = models.CharField(max_length=50,unique=True)

	simbol = models.CharField(max_length=5,unique=True)

	def save(self,*args,**kwargs):
		from datetime import time
		if self.start >= self.end:
			WorkTime.objects.create(title=self.title+'2',simbol='-',start=time(0,0),end=self.end)

			self.end = time(23,59)
		super(WorkTime,self).save(*args,**kwargs)


	def __unicode__(self):
		return self.title


class Staff(models.Model):
	name = models.CharField(max_length=40,unique=True)

	user = models.OneToOneField(User,null=True,blank=True)

	def __unicode__(self):
		return self.name


class StaffSchedule(Date):
	staff = models.ForeignKey(Staff,unique_for_date='date')

	worktime = models.ForeignKey(WorkTime)

	leader = models.BooleanField(default=False)

	phoner = models.BooleanField(default=False)

	def __unicode__(self):
		return self.strfdate()

class NgShift(Date):
	staff = models.ForeignKey(Staff,unique_for_date='date')

	ng_shift = models.ManyToManyField(WorkTime)

	
	def ng_values(self):
		values = self.ng_shift.values_list('title')
		
		return ",".join( reduce( lambda x,y:x + y ,values ) )
	

	def __unicode__(self):
		return self.staff.name
