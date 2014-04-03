from django.db import models
from django.contrib.auth.models import User,Group
from django.core.validators import MaxValueValidator,MinValueValidator


class GroupSchedule(models.Model):
	group = models.OneToOneField(Group)

	owner = models.OneToOneField(User)

	start_point = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(31),MinValueValidator(1),])

	def get_calendar(self,year,month):
		from calendar import Calendar

		from datetime import date
		cal_start = date( year,month,self.start_point )
		cal_end = cal_start.replace(month=cal_start.month+1)
		
		this_month = list( Calendar().itermonthdates( year,month ) )
		next_month = list( Calendar().itermonthdates( year,month+1 ) )
		
		wcal = this_month + next_month
		wcal_list = wcal[wcal.index(cal_start):wcal.index(cal_end)]

		return sorted( set(wcal_list),key=wcal_list.index )

	def __unicode__(self):
		return self.group.name
