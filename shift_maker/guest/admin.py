from django.contrib import admin
from guest.models import Guest,GuestSchedule
from schedule.admin import DateAdmin,TimeTableAdmin


class GuestScheduleAdmin(DateAdmin,TimeTableAdmin):
	list_display = ('schedule_date','guest','time_table',)	# schedule_date & time_table from schedule/admin

	list_filter = ['date','guest',]

admin.site.register(GuestSchedule,GuestScheduleAdmin)


class GuestAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Guest,GuestAdmin)
