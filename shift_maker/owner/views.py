from django.shortcuts import render
from django.contrib.auth.models import User


def new_owner(req):

	error_msg = None

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
				try:
					owner = User.objects.create_user(username=name,password=password)
				except IntegrityError:
					error_msg = "You can not use this name!"

	return render(req,'owner/new_owner.html',{'error_msg':error_msg,})
