from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

month_url = r'(?P<year_num>\d+)\-(?P<month_num>\d+)'
day_url = r'(?P<day_num>\d+)'

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'schedule.views.home', name="Please wait..."),

	 url(r'^%s/$' % (month_url,),'schedule.views.a_month',name="Month"),
	 url(r'^%(month)s/%(day)s/$' % {'month':month_url,'day':day_url,},'schedule.views.a_day',name="Day"),

    url(r'^admin/', include(admin.site.urls)),
)
