from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


class Date(models.Model):

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


class Month(models.Model):
	year = models.PositiveIntegerField(validators=[MinValueValidator(1),])

	month = models.PositiveIntegerField(validators=[MaxValueValidator(12),MinValueValidator(1),])

	def get_calendar(self):
		from calendar import Calendar
		year,month = self.year,self.month

		from datetime import date
		cal_start = date( year,month,15 )
		cal_end = cal_start.replace(month=cal_start.month+1)
		
		this_month = list( Calendar().itermonthdates( year,month ) )
		next_month = list( Calendar().itermonthdates( year,month+1 ) )
		
		wcal = this_month + next_month
		wcal_list = wcal[wcal.index(cal_start):wcal.index(cal_end)]

		return sorted( set(wcal_list),key=wcal_list.index )

	class Meta:
		unique_together = ( ('year','month',), )

		abstract = True
