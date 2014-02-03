from django.contrib import admin
from models import WorkTime,DateAndStaff,StaffShift,DateAndGuest,GuestPlan

admin.site.register(WorkTime)
admin.site.register(DateAndStaff)
admin.site.register(StaffShift)
admin.site.register(DateAndGuest)
admin.site.register(GuestPlan)
