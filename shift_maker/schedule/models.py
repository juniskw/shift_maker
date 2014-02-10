from django.db import models


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
