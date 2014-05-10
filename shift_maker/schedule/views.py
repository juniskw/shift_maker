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
	year,month = int(year_num),int(month_num)

	from calendar import Calendar
	month_cal = Calendar().monthdayscalendar(year,month)

	return render( req,'schedule/a_month.html',{
			  'year':year_num,
			  'month':month_num,
			  'month_cal':month_cal,
	}, )


@login_required
def a_month_shift(req,year_num,month_num):
	from owner.models import GroupSchedule
	from schedule.models import WorkTime,MonthShift,StaffSchedule,NgShift,GuestSchedule
	from datetime import date

	year,month = int(year_num),int(month_num)

	try:
		groupschedule = GroupSchedule.objects.get(owner=req.user)
	except GroupSchedule.DoesNotExist:
		return redirect('/owner/schedule/edit')

	if req.method == 'POST':
		posted = req.POST
		s_year,s_month,s_day = int(posted['year']),int(posted['month']),int(posted['day'])
		s_date = date( year=s_year,month=s_month,day=s_day )

		try:
			s_schedule = StaffSchedule.objects.get( date=s_date,staff=int(posted['staff']) )
		except StaffSchedule.DoesNotExist:
			from staff.models import Staff
			s_schedule = StaffSchedule(date=s_date)
			s_schedule.staff = Staff.objects.get( id=int(posted['staff']) )

		s_schedule.monthshift,created = MonthShift.objects.get_or_create(year=year,month=month,groupschedule=req.user.groupschedule)

		s_schedule.worktime = WorkTime.objects.get( id=int(posted['shift']) )

		s_schedule.save()

	#try:
	#	monthshift = groupschedule.monthshift_set.get(year=year,month=month,groupschedule=req.user.groupschedule)	#
	#except MonthShift.DoesNotExist:
	#	monthshift = None
	monthshift,created = groupschedule.monthshift_set.get_or_create(year=year,month=month,groupschedule=req.user.groupschedule)	#

	month_cal = groupschedule.get_calendar(year,month)

	def get_month_schedules(sch,cal):
		month_schedules = list()
		for day in cal:
			try:
				month_schedules.extend( sch.objects.filter(date=day) )
			except sch.DoesNotExist:
				continue
		return month_schedules

	staffschedules = get_month_schedules(StaffSchedule,month_cal)

	return render(req,'schedule/a_month_shift.html',{
		'url_plus':'shift/',
		'year':year_num,
		'month':month_num,
		'month_cal':month_cal,
		'monthshift':monthshift,
		'weekdays':['月','火','水','木','金','土','日',],
		'staffs':groupschedule.staff_set.order_by('id'),
		'worktimes':groupschedule.worktime_set.order_by('id'),
	})


@login_required
def new_worktime(req):
	from schedule.models import WorkTime
	from datetime import time

	if req.method == 'POST':
		posted = req.POST

		worktime = WorkTime()

		def get_time(pstd,hour,minute):
			hour,minute = pstd[hour],pstd[minute]
			return time( int(hour),int(minute) )

		worktime.groupschedule = req.user.groupschedule
		worktime.title = posted['title']
		worktime.simbol = posted['simbol']
		worktime.start = get_time(posted,'start_h','start_m')
		worktime.end = get_time(posted,'end_h','end_m')

		worktime.save()

		return redirect('/')

	temp = 'schedule/new_worktime.html'
	contxt = {}

	return render(req,temp,contxt)
