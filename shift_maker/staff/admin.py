from django.contrib import admin
from staff.models import WorkTime,Staff,StaffSchedule,NgShift
from schedule.admin import DateAdmin,TimeTableAdmin

class WorkTimeAdmin(TimeTableAdmin):
	list_display = ('title','time_table',)	# time_table from schedule/admin

admin.site.register(WorkTime,WorkTimeAdmin)


class StaffAdmin(admin.ModelAdmin):
	list_display = ('name','ng_list',)

	def ng_list(self,obj):
		ngs = ""

		for ng in obj.ngshift_set.all():
			ngs += "%s(%s) ," % ( ng.date,ng.ng_values(), )

		return ngs

	ng_list.short_description = 'NGs'

admin.site.register(Staff,StaffAdmin)


class StaffScheduleAdmin(DateAdmin):
	list_display = ('schedule_date','staff','shift',)	# schedule_date from schedule/admin

	list_filter = ['date','staff',]

admin.site.register(StaffSchedule,StaffScheduleAdmin)#,StaffScheduleAdmin)


class NgShiftAdmin(DateAdmin):
	list_display = ('staff','schedule_date','get_values')	# schedule_date from schedule/admin

	def get_values(self,obj):
		return obj.ng_values()

	get_values.short_description = 'NgShift'

	list_filter = ['date','staff',]

admin.site.register(NgShift,NgShiftAdmin)
