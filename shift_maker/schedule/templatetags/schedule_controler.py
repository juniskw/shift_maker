from django import template

register = template.Library()

def get_schedule(sch_model,day_num,staff_id):
	return month_num+'month'

	import datetime
	sche_date = datetime.date( year=int(year_num),month=int(month_num),day=int(day_num) )
	try:
		schedule = sch_model.objects.get( date=sch_date,staff=int(staff_id) )
		return schedule
	except schedule.DoesNotExist:
		return None


register.filter('get_schedule',get_schedule)
