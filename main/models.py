from django.db import models

# Create your models here.
class user_info(models.Model):
  user_name = models.CharField(max_length=20)
  is_driver = models.BooleanField(default=False, null=False)
  hashed_pass = models.CharField(max_length=50)
  region = models.CharField(max_length=50, null=False)
  total_socore = models.FloatField(max_length=50)

class request(models.Model):
  user_id = models.IntegerField()
  title = models.CharField(max_length=100)
  matching_complete = models.IntegerField(default=0)
  request_complete = models.IntegerField(default=0)
  share_or_not = models.IntegerField(default=0)
  post_time = models.DateTimeField()
  text = models.CharField(max_length=100, null=False)
  departure_place = models.CharField(max_length=100)
  destination_place = models.CharField(max_length=100)
  delivery_date = models.CharField(max_length=50)
  asking_price = models.IntegerField()
  driver_evaluation = models.FloatField()
  client_evaluation = models.FloatField()

