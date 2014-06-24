from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

month_url = r'(?P<year_num>\d+)\-(?P<month_num>\d+)'
day_url = r'(?P<day_num>\d+)'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('owner.views',
	url(r'^login/$','log_in',name="LogIn"),
	url(r'^logout/$','log_out',name="LogOut"),
	url(r'^owner/new/$','new_owner',name="newOwner"),
	url(r'^owner/schedule/edit/$','edit_groupschedule',name="EditSchedule"),
)

urlpatterns += patterns('schedule.views',
   url(r'^$', 'home', name="Please wait..."),

	url(r'^%s/$' % (month_url,),'a_month',name="Month"),
	url(r'^%s/shift/$' % (month_url,),'a_month_shift',name="MonthShift"),
	url(r'^worktime/new/$','new_worktime',name="NewWorkTime"),
	url(r'^%s/shift/edit/$' % (month_url,),'edit_shift'),
)

urlpatterns += patterns('staff.views',
	url(r'^staff/new/$','new_staff',name="NewStaff"),
)
