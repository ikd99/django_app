from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import IntegerField

# Create your models here.
class user_info(models.Model):
  user_name = models.CharField(max_length=20, null=False)
  is_driver = models.BooleanField(default=False, null=False)
  hashed_pass = models.IntegerField(null=False)
  region = models.CharField(max_length=50, null=False)
  total_socore = models.FloatField(max_length=50)

class requests(models.Model):
  client_id = models.ForeignKey(user_info, on_delete=models.CASCADE)
  title = models.CharField(max_length=100, null=False)
  matching_complete = models.BooleanField(default=False)
  request_complete = models.BooleanField(default=False)
  share_or_not = models.BooleanField(default=False)
  post_time = models.DateTimeField(null=False)
  text = models.TextField(max_length=1000, null=False)
  departure_place = models.CharField(max_length=100, null=False)
  destination_place = models.CharField(max_length=100, null=False)
  delivery_date = models.DateTimeField(null=False)
  asking_price = models.IntegerField(null=False)
  driver_evaluation = models.FloatField()
  client_evaluation = models.FloatField()

class messages(models.Model):
  user_id = models.ForeignKey(user_info, on_delete=models.SET_NULL, null=True)
  post_id = models.ForeignKey(requests, on_delete=models.CASCADE)
  mess = models.TextField(max_length=1000, null=False)

class payment(models.Model):
  post_id = models.ForeignKey(requests, on_delete=models.PROTECT)
  payment_amount = models.IntegerField(null=False)

class favorite(models.Model):
  user_id = models.ForeignKey(user_info, on_delete=models.CASCADE)
  post_id = models.ForeignKey(requests, on_delete=models.CASCADE)