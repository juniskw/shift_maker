#coding:utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect

#### views ####
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
	from datetime import date

	year,month = int(year_num),int(month_num)

	try:
		groupschedule = GroupSchedule.objects.get(owner=req.user)
	except GroupSchedule.DoesNotExist:
		return redirect('/owner/schedule/edit')

	monthshift,created = groupschedule.monthshift_set.get_or_create(year=year,month=month,groupschedule=req.user.groupschedule)


	month_cal = groupschedule.get_calendar(year,month)

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

#### ajax ####
@login_required
def edit_shift(req,year_num,month_num):
	from schedule.models import WorkTime,MonthShift,StaffSchedule
	from staff.models import Staff	#
	from datetime import date

	if req.method == 'POST':
		monthshift,created = MonthShift.objects.get_or_create(year=int(year_num),month=int(month_num),groupschedule=req.user.groupschedule)

		posted = req.POST
		s_year,s_month,s_day = int(posted['year']),int(posted['month']),int(posted['day'])
		s_date = date( year=s_year,month=s_month,day=s_day )
	
		s_staff = Staff.objects.get( id=int(posted['staff_id']) )

		try:
			s_schedule = StaffSchedule.objects.get( date=s_date,staff=s_staff )
		except StaffSchedule.DoesNotExist:
			s_schedule = StaffSchedule(date=s_date,staff=s_staff)

		s_schedule.monthshift = monthshift

		s_schedule.worktime = WorkTime.objects.get( id=int(posted['worktime_id']) )

		s_schedule.save()

		from django.http import HttpResponse
		return HttpResponse( s_schedule.worktime.simbol,content_type="text/plain" )

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
