from django.shortcuts import render


def new_staff(req):
	from staff.models import Staff

	if req.method == 'POST':
		posted = req.POST

		staff = Staff()

		staff.name = posted['name']

		staff.save()

	temp = 'staff/new_staff.html'
	contxt = {}

	return render(req,temp,contxt)


def new_worktime(req):
	from staff.models import WorkTime
	from datetime import time

	if req.method == 'POST':
		posted = req.POST

		worktime = WorkTime()

		def get_time(pstd,hour,minute):
			hour,minute = pstd[hour],pstd[minute]
			return time( int(hour),int(minute) )

		worktime.title = posted['title']
		worktime.simbol = posted['simbol']
		worktime.start = get_time(posted,'start_h','start_m')
		worktime.end = get_time(posted,'end_h','end_m')

		worktime.save()

	temp = 'staff/new_worktime.html'
	contxt = {}

	return render(req,temp,contxt)
