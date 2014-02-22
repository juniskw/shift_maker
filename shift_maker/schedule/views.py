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


	tmp = 'schedule/a_month_shift.html'

	month_cal = Calendar().itermonthdays2( int(year_num),int(month_num) )

	contxt = {
		'url_plus':'shift/',
		'year':year_num,
		'month':month_num,
		'month_cal':list(month_cal),
		'staffs':Staff.objects.all().order_by('id'),
		'worktimes':WorkTime.objects.all().order_by('id'),
		'staffschedules':StaffSchedule.objects.all().order_by('date'), #filter(date.month=month_num)
		#'ngshifts':NgShift.objects.all().order_by('date'),
		#'guests':Guest.objects.all().order_by('name'),
		#'guestschedules':GuestSchedule.objects.all().order_by('date'),		  
	}

	return render(req,tmp,contxt)
