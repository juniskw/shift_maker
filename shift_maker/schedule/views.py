#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(req):
	from datetime import datetime
	
	now = datetime.now()

	return HttpResponseRedirect( '/%s-%s/shift/' % (now.year,now.month,) )


def a_month(req,year_num,month_num):
	from staff.models import StaffSchedule
	from calendar import Calendar

	tmp = 'schedule/a_month.html'

	month_cal = Calendar().monthdayscalendar( int(year_num),int(month_num) )

	cntxt = {
		'year':year_num,
		'month':month_num,
		'month_cal':month_cal,
	}

	return render( req,tmp,cntxt )


def a_month_shift(req,year_num,month_num):
	from staff.models import *
	from guest.models import *
	from calendar import Calendar
	from datetime import date

	if req.method == 'POST':
		p_resp = req.POST

		s_date = date( year=int(year_num),month=int(month_num),day=int(p_resp['day']) )

		try:
			s_schedule = StaffSchedule.objects.get( date=s_date,staff=int(p_resp['staff']) )
		except StaffSchedule.DoesNotExist:
			s_schedule = StaffSchedule(date=s_date)
			s_schedule.staff = Staff.objects.get( id=int(p_resp['staff']) )

		s_schedule.shift = WorkTime.objects.get( id=int(p_resp['shift']) )

		s_schedule.save()

	month_cal = Calendar().itermonthdates( int(year_num),int(month_num) )

	tmp = 'schedule/a_month_shift.html'

	contxt = {
		'url_plus':'shift/',
		'year':year_num,
		'month':month_num,
		'month_cal':list(month_cal),
		'weekdays':['月','火','水','木','金','土','日',],
		'staffs':Staff.objects.all().order_by('id'),
		'worktimes':WorkTime.objects.all().order_by('id'),
		'staffschedules':StaffSchedule.objects.all().order_by('staff'),
	}

	return render(req,tmp,contxt)
