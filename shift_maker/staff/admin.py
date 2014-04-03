from django.contrib import admin
from staff.models import Staff


class StaffAdmin(admin.ModelAdmin):
	list_display = ('name','ng_list',)

	def ng_list(self,obj):
		ngs = ""

		for ng in obj.ngshift_set.all():
			ngs += "%s(%s) ," % ( ng.date,ng.ng_values(), )

		return ngs

admin.site.register(Staff,StaffAdmin)
