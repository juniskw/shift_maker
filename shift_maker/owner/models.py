from django.db import models
from django.contrib.auth.models import User,Group
from django.core.validators import MaxValueValidator,MinValueValidator


class GroupSchedule(models.Model):
	group = models.OneToOneField(Group)

	owner = models.OneToOneField(User)

	start_point = models.PositiveIntegerField(default=1,validators=[MaxValueValidator(31),MinValueValidator(1),])
