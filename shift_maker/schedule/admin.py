from django.contrib import admin
from schedule.models import WorkTime,MonthShift,StaffSchedule,NgShift,GuestSchedule


#### base classes ####

class DateAdmin(admin.ModelAdmin):

	def schedule_date(self,obj):
		return obj.strfdate()

	date_hierarchy = 'date'


class TimeTableAdmin(admin.ModelAdmin):

	def time_table(self,obj):
		return obj.strftimetable()


#### main classes ####

###### staff ######
class MonthScheduleAdmin(admin.ModelAdmin):
	list_display = ('year','month','groupschedule','completed',)

admin.site.register(MonthShift)


class WorkTimeAdmin(TimeTableAdmin):
	list_display = ('title','time_table',)	# time_table from schedule/admin

admin.site.register(WorkTime,WorkTimeAdmin)


class StaffScheduleAdmin(DateAdmin):
	list_display = ('schedule_date','staff','worktime',)	# schedule_date from schedule/admin

	list_filter = ['date','staff',]

admin.site.register(StaffSchedule,StaffScheduleAdmin)#,StaffScheduleAdmin)


class NgShiftAdmin(DateAdmin):
	list_display = ('staff','schedule_date','get_values')	# schedule_date from schedule/admin

	def get_values(self,obj):
		return obj.ng_values()

	list_filter = ['date','staff',]

admin.site.register(NgShift,NgShiftAdmin)


###### guest ######
class GuestScheduleAdmin(DateAdmin,TimeTableAdmin):
	list_display = ('schedule_date','guest','time_table',)	# schedule_date & time_table from schedule/admin

	list_filter = ['date','guest',]

admin.site.register(GuestSchedule,GuestScheduleAdmin)
