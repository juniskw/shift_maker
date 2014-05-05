from django.contrib import admin
from guest.models import Guest


class GuestAdmin(admin.ModelAdmin):
	list_display = ('name','get_schedules',)
	list_filter = ('groupschedule',)

	def get_schedules(self,obj):
		schedules = ""

		for schedule in obj.guestschedule_set.all():
			schedules += "%s(%s) ," % ( schedule.date,schedule.strftimetable(), )

		return schedules

	get_schedules.short_description = 'Schedules'		

admin.site.register(Guest,GuestAdmin)
