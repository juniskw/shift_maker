from django.contrib import admin
from owner.models import GroupSchedule


class GroupScheduleAdmin(admin.ModelAdmin):
	list_display = ('group','owner',)


admin.site.register(GroupSchedule,GroupScheduleAdmin)
