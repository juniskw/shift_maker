from django import template

register = template.Library()


@register.filter(name='index_is')
def varindex(val,arg):
	return val[arg]

@register.filter(name='date_is')
def date_filter(val,arg):
	return val.filter(date=arg)

@register.filter(name='staff_is')
def staff_get(val,arg):
	from staff.models import StaffSchedule
	try:
		return val.get(staff=arg)
	except StaffSchedule.DoesNotExist:
		return None
