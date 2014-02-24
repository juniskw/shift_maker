from django import template

register = template.Library()

@register.filter(name='staff_is')
def staff_filter(val,arg):
	return val.filter(staff=arg)

@register.filter(name='date_is')
def date_get(val,arg):
	from staff.models import StaffSchedule
	try:
		obj = val.get(date=arg)
		return obj
	except StaffSchedule.DoesNotExist:
		return None
