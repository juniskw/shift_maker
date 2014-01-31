from django.contrib import admin
from making.models import Day,WorkTime,Staff,Visitor,VisitSchedule

class StaffAdmin(admin.ModelAdmin):
	fields = ['name','workstyle','drive']

admin.site.register(Day)

admin.site.register(WorkTime)
admin.site.register(Staff)

admin.site.register(Visitor)
admin.site.register(VisitSchedule)
