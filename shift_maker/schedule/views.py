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

		s_date = date( year=year,month=month,day=int(posted['day']) )

		try:
			s_schedule = StaffSchedule.objects.get( date=s_date,staff=int(posted['staff']) )
		except StaffSchedule.DoesNotExist:
			from staff.models import Staff
			s_schedule = StaffSchedule(date=s_date)
			s_schedule.staff = Staff.objects.get( id=int(posted['staff']) )

		s_schedule.worktime = WorkTime.objects.get( id=int(posted['shift']) )

		s_schedule.save()

	try:
		monthshift = groupschedule.monthshift_set.get(year=year,month=month)	#
	except MonthShift.DoesNotExist:
		pass

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
		'weekdays':['月','火','水','木','金','土','日',],
		'staffs':groupschedule.staff_set.order_by('id'),
		'worktimes':groupschedule.worktime_set.order_by('id'),
	})
