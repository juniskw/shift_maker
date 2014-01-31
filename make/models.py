#!/usr/bin/env python
#coding:utf-8

class Staff_Pattern(object):

	def __init__(self,pattern,request):
		self.pattern = pattern
		self.request = request

class Staff(object):
	# from calendar import monthrange
	def __init__(self,name,\
					day_work=True,drive=False,night_work=False,\
					):#request=[0,]*monthrange[1]):	 requestは辞書型にすべき？
		self.name = name
		self.day_work = day_work
		self.night_work = night_work
		self.drive = drive
		# self.request = request

	def info(self):
		print("\n####staff-info####\nname = %s\nday_work = %s\nnight_work = %s\ndrive = %s\n##################\n" % (self.name,self.day_work,self.night_work,self.drive) )

"""
class Guest(object):

	def __init__(self,name,patterns):
		self.name = name
		self.patterns = patterns
"""

#class StaffPatterns():
#class Guest_Patterns(object):
