from django.shortcuts import render
from django.http import HttpResponseRedirect

def home(req):
	from datetime import datetime
	
	now = datetime.now()

	return HttpResponseRedirect( '/%s-%s/' % (now.year,now.month,) )


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

	tmp = 'schedule/a_month_shift.html'

	month_cal = Calendar().itermonthdays2( int(year_num),int(month_num) )

	contxt = {
		'url_plus':'shift/',
		'year':year_num,
		'month':month_num,
		'month_cal':list(month_cal),
		'staffs':Staff.objects.order_by('name'),
		'staffschedules':StaffSchedule.objects.all().order_by('date'),
		'ngshifts':NgShift.objects.all().order_by('date'),
		'guests':Guest.objects.all().order_by('name'),
		'guestschedules':GuestSchedule.objects.all().order_by('date'),		  
	}

	return render(req,tmp,contxt)
