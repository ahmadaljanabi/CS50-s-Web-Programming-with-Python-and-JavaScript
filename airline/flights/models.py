from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    duration = models.IntegerField()
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
