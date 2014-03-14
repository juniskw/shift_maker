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

	class Meta:
		abstract = True
