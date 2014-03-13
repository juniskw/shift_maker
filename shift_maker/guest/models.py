from django.db import models
from schedule.models import Date,TimeTable,MonthSchedule


class Guest(models.Model):
	name = models.CharField(max_length=40,unique=True)

	def __unicode__(self):
		return self.name


class GuestSchedule(Date,TimeTable):
	guest = models.ForeignKey(Guest,unique_for_date='date')

	def save(self,*args,**kwargs):
		self.parent = MonthSchedule.objects.get_or_create(year=self.date.year,month=self.date.month)
		super(StaffSchedule,self).save(*args,**kwargs)

	def __unicode__(self):
		return self.strfdate()


class GuestTime(TimeTable):
	date = models.OneToOneField(GuestSchedule)
