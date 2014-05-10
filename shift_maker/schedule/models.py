from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from owner.models import GroupSchedule
from staff.models import Staff
from guest.models import Guest


#### base classes ####

class Date(models.Model):
	monthshift = models.ForeignKey('MonthShift')

	date = models.DateField()

	def strfdate(self):
		return self.date.strftime('%Y/%m/%d,%a')

	class Meta:
		abstract = True	# This class is not make table


class TimeTable(models.Model):
	start = models.TimeField(default='00:00')
	end = models.TimeField(default='00:00')

	def strftimetable(self):
		timef = '%H:%M'
		start,end = self.start,self.end
		return "%s ~ %s" % ( start.strftime(timef),end.strftime(timef) )

	class Meta:
		abstract = True	# This class is not make table


#### main classes ####

###### staff ######
class MonthShift(models.Model):
	year = models.PositiveIntegerField(validators=[MinValueValidator(1),])

	month = models.PositiveIntegerField(validators=[MaxValueValidator(12),MinValueValidator(1),])

	groupschedule = models.ForeignKey(GroupSchedule)

	completed = models.BooleanField(default=False)

	class Meta:
		unique_together = ( ('year','month','groupschedule',), )


class WorkTime(TimeTable):
	groupschedule = models.ForeignKey(GroupSchedule)

	title = models.CharField(max_length=50,unique=True)

	simbol = models.CharField(max_length=5,unique=True)

	def save(self,*args,**kwargs):
		from datetime import time
		if self.start >= self.end:
			WorkTime.objects.create(groupschedule=self.groupschedule,title=self.title+'2',simbol='-',start=time(0,0),end=self.end)

			self.end = time(23,59)
		super(WorkTime,self).save(*args,**kwargs)

	class Meta:
		unique_together = ( ('groupschedule','title',),('groupschedule','simbol',), )

	def __unicode__(self):
		return self.title


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


###### guest ######
class GuestSchedule(Date,TimeTable):
	guest = models.ForeignKey(Guest,unique_for_date='date')

	def __unicode__(self):
		return self.strfdate()
