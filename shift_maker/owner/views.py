from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def log_in(req):

	if req.user.is_authenticated():
		return redirect('/')	#

	error_msg = ""

	if req.method == 'POST':
		posted = req.POST
		name,password = posted['name'],posted['password']

		user = authenticate(username=name,password=password)

		if user is not None:
			if user.is_active:
				login(req,user)

				return redirect('/')
			else:
				error_msg = "This account is not active..."
		else:
			error_msg = "Log in failed...."
				
	return render(req,'owner/log_in.html',{'error_msg':error_msg}) 


def log_out(req):
	logout(req)

	return redirect('/login/')


def new_owner(req):

	if req.user.is_authenticated():
		return redirect('/logout/')	#

	error_msg = ""

	if req.method == 'POST':
		posted = req.POST
		name,password = posted['name'],posted['password']

		if password != posted['pass_check']:
			error_msg = "Password check is failed!"
		else:
			if len(password) < 6:
				error_msg = "Password need over 6 letters!"
			else:
				from django.db import IntegrityError
				from django.contrib.auth.models import User
				try:
					owner = User.objects.create_user(username=name,password=password)
				except IntegrityError:
					error_msg = "You can not use this name!"

	return render(req,'owner/new_owner.html',{'error_msg':error_msg,})


@login_required
def create_groupschedule(req):
	from django.contrib.auth.models import Group
	from owner.models import GroupSchedule

	if req.method == 'POST':
		posted = req.POST

		new_group = Group(name=posted['name'])
		new_groupschedule = GroupSchedule(start_point=int(posted['start_point']),owner=req.user)

		new_group.save()

		new_groupschedule.group = new_group
		new_groupschedule.save()

	return render(req,'owner/create_groupschedule.html')
