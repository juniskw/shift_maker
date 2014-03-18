from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

month_url = r'(?P<year_num>\d+)\-(?P<month_num>\d+)'
day_url = r'(?P<day_num>\d+)'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

owner_url = 'owner'
urlpatterns += patterns('owner.views',
	url(r'^login/$','log_in',name="LogIn"),
	url(r'^logout/$','log_out',name="LogOut"),
	url(r'^%s/new/$' % owner_url,'new_owner',name="newOwner"),
)

urlpatterns += patterns('schedule.views',
    url(r'^$', 'home', name="Please wait..."),

	 url(r'^%s/$' % (month_url,),'a_month',name="Month"),
	 url(r'^%s/shift/$' % (month_url,),'a_month_shift',name="MonthShift"),
)

urlpatterns += patterns('staff.views',
	 url(r'^staff/new/$','new_staff',name="NewStaff"),
	 url(r'^worktime/new/$','new_worktime',name="NewWorkTime"),
)
