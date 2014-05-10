from django.shortcuts import render,redirect


def new_staff(req):
	from staff.models import Staff

	if req.method == 'POST':
		posted = req.POST

		staff = Staff()

		staff.groupschedule = req.user.groupschedule
		staff.name = posted['name']

		staff.save()

		return redirect('/')

	temp = 'staff/new_staff.html'
	contxt = {}

	return render(req,temp,contxt)
