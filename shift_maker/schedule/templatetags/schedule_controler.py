from django import template

register = template.Library()


@register.filter
def index_is(val,arg):
	return val[arg]

#### filters ####
@register.filter
def monthshift_filter(val,arg):
	return val.filter(monthshift=arg)

@register.filter
def date_filter(val,arg):
	return val.filter(date=arg)

@register.filter
def staff_filter(val,arg):
	return val.filter(staff=arg)

@register.filter	# for staff
def worktime_filter(val,arg):
	return val.filter(worktime=arg)

#### gets ####
@register.filter
def staff_get(val,arg):
	from schedule.models import StaffSchedule
	try:
		return val.get(staff=arg)
	except StaffSchedule.DoesNotExist:
		return None

@register.filter
def date_get(val,arg):
	from schedule.models import StaffSchedule
	try:
		return val.get(date=arg)
	except StaffSchedule.DoesNotExist:
		return None
