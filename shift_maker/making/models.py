#coding:utf-8

from django.db import models

#### Schedule ####
class Day(models.Model):
	date = models.DateField("Day of:")

	staff = models.ManyToManyField('Staff',related_name='day')
	visitor = models.ManyToManyField('VisitSchedule',related_name='day')

	events = models.CharField("Event:",max_length=100)

	def __unicode__(self):
		return self.date.strftime("%Y/%m/%d,%a %H:%S")

#### Staff ####
class WorkTime(models.Model):
	title = models.CharField("Shift name:",max_length=50)

	start_time = models.TimeField("Work start:")
	end_time = models.TimeField("Work end:")

	staff = models.ManyToManyField('Staff',related_name='workstyle')

	def __unicode__(self):
		return self.title

class Staff(models.Model):
	name = models.CharField("Name:",max_length=40)

	drive = models.BooleanField("Driver skill")

	def __unicode__(self):
		return self.name

#### Visitor ####
class Visitor(models.Model):
	l_name = models.CharField("Last name:",max_length=20)
	f_name = models.CharField("First name:",max_length=20)

	def __unicode__(self):
		return "%s %s" % (self.l_name,self.f_name,)

class VisitSchedule(models.Model):
	visitor = models.ForeignKey(Visitor,related_name='schedule')

	come_time = models.DateTimeField("Come time:")
	back_time = models.DateTimeField("Back time:")

	def __unicode__(self):
		return "<%s> ~ <%s> [%s]" % (self.come_time.strftime("%Y/%m/%d,%a %H:%S"),self.back_time.strftime("%Y/%m/%d,%a %H:%S"),self.visitor,)
