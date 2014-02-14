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
		'month':month_num,
		'month_cal':month_cal,
	}

	return render( req,tmp,cntxt )
