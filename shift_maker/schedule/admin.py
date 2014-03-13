from django.contrib import admin
from schedule.models import MonthSchedule


class DateAdmin(admin.ModelAdmin):

	def schedule_date(self,obj):
		return obj.strfdate()

	schedule_date.short_description = 'Date'

	date_hierarchy = 'date'

class TimeTableAdmin(admin.ModelAdmin):

	def time_table(self,obj):
		return obj.strftimetable()

	time_table.short_description = 'TimeTable'


admin.site.register(MonthSchedule)
