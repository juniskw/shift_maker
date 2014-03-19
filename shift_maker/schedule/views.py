#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect


@login_required
def home(req):
	from datetime import datetime
	
	now = datetime.now()

	return redirect( '/%s-%s/shift/' % (now.year,now.month,) )


@login_required
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


@login_required
def a_month_shift(req,year_num,month_num):
	from staff.models import WorkTime,MonthShift,Staff,StaffSchedule,NgShift
	from guest.models import Guest,GuestSchedule
	from calendar import Calendar
	from datetime import date

	year,month = int(year_num),int(month_num)

	if req.method == 'POST':
		posted = req.POST

		s_date = date( year=year,month=month,day=int(posted['day']) )

		try:
			s_schedule = StaffSchedule.objects.get( date=s_date,staff=int(posted['staff']) )
		except StaffSchedule.DoesNotExist:
			s_schedule = StaffSchedule(date=s_date)
			s_schedule.staff = Staff.objects.get( id=int(posted['staff']) )

		s_schedule.worktime = WorkTime.objects.get( id=int(posted['shift']) )

		s_schedule.save()

	monthshift = req.user.groupschedule.monthshift_set.get(year=year,month=month)	#

	month_cal = monthshift.get_calendar()

	def get_month_schedules(sch,cal):
		month_schedules = list()
		for day in cal:
			try:
				month_schedules.extend( sch.objects.filter(date=day) )
			except sch.DoesNotExist:
				continue
		return month_schedules

	staffschedules = get_month_schedules(StaffSchedule,month_cal)

	tmp = 'schedule/a_month_shift.html'

	contxt = {
		'url_plus':'shift/',

		'year':year_num,
		'month':month_num,

		'month_cal':month_cal,
		'weekdays':['月','火','水','木','金','土','日',],

		'staffs':Staff.objects.order_by('id'),
		'worktimes':WorkTime.objects.order_by('id'),
		'staffschedules':GroupSchedule.staff_set,
	}

	return render(req,tmp,contxt)
