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
def edit_groupschedule(req):
	from django.contrib.auth.models import Group
	from owner.models import GroupSchedule
		
	try:
		groupschedule = GroupSchedule.objects.get(owner=req.user)
		group = groupschedule.group
	except GroupSchedule.DoesNotExist:
		groupschedule = GroupSchedule(owner=req.user)
		group = Group()

	if req.method == 'POST':
		posted = req.POST

		group.name = posted['name']
		group.save()

		groupschedule.group = group
		groupschedule.start_point = int(posted['start_point'])
		groupschedule.save()

		#try:
			#groupschedule = GroupSchedule.objects.get(owner=req.user)
			#group = groupschedule.group
			#group.name = posted['name']
			#group.save()
		#except GroupSchedule.DoesNotExist:
			#group = Group.objects.create(name=posted['name'])
			#groupschedule = GroupSchedule(owner=req.user,group=group,start_point=int(posted['start_point']))

		#groupschedule.start_point = int(posted['start_point'])
		#groupschedule.save()

	return render(req,'owner/edit_groupschedule.html',{
		'group_name':group.name,
		'start_point':groupschedule.start_point,
		'select_choices':(1,5,10,15,20,25,),
	})
