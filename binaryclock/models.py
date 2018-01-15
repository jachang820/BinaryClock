from django.db import models

# Create your models here.
class User(models.Model):
	cred = models.TextField('credentials')
	email = models.CharField(max_length=32)
	uid = models.CharField(primary_key=True,max_length=32)
	logged_in = models.BooleanField()

	class Meta:
		ordering = ["email"]

	def __str__(self):
		return self.user_name

class Event(models.Model):
	eid = models.CharField(primary_key=True, max_length=32)
	start_time = models.DateTimeField('start.dateTime')
	start_zone = models.CharField('start.timeZone',max_length=32)
	end_time = models.DateTimeField('end.dateTime')
	end_zone = models.CharField('end.timeZone',max_length=32)
	summary = models.TextField('summary')
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		ordering = ["start_time"]

	def __str__(self):
		return self.summary
