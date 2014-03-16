from django.db import models
from django.contrib.auth.models import User
from schedule.models import Date,TimeTable,Month
from owner.models import GroupSchedule


class MonthShift(Month):
	groupschedule = models.ForeignKey(GroupSchedule)

	completed = models.BooleanField(default=False)

	def get_calendar(self):
		from calendar import Calendar
		year,month = self.year,self.month

		from datetime import date
		cal_start = date( year,month,self.groupschedule.start_point )
		cal_end = cal_start.replace(month=cal_start.month+1)
		
		this_month = list( Calendar().itermonthdates( year,month ) )
		next_month = list( Calendar().itermonthdates( year,month+1 ) )
		
		wcal = this_month + next_month
		wcal_list = wcal[wcal.index(cal_start):wcal.index(cal_end)]

		return sorted( set(wcal_list),key=wcal_list.index )

	class Meta:
		unique_together = ( ('year','month','groupschedule',), )


class WorkTime(TimeTable):
	groupschedule = models.ForeignKey(GroupSchedule)

	title = models.CharField(max_length=50,unique=True)

	simbol = models.CharField(max_length=5,unique=True)

	def save(self,*args,**kwargs):
		from datetime import time
		if self.start >= self.end:
			WorkTime.objects.create(title=self.title+'2',simbol='-',start=time(0,0),end=self.end)

			self.end = time(23,59)
		super(WorkTime,self).save(*args,**kwargs)

	class Meta:
		unique_together = ( ('groupschedule','title',),('groupschedule','simbol',), )

	def __unicode__(self):
		return self.title


class Staff(models.Model):
	groupschedule = models.ForeignKey(GroupSchedule)

	name = models.CharField(max_length=40)

	user = models.OneToOneField(User,null=True,blank=True)

	class Meta:
		unique_together = ( ('name','groupschedule',), )

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
