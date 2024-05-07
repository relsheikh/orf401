from django.db import models # type: ignore

class Person(models.Model):
  first_name = models.CharField(max_length=64)
  origination = models.CharField(max_length=64)
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)


    #def __str__(self):
    #    return f"{self.origination_state} to {self.destination_city}, {self.destination_state}"

