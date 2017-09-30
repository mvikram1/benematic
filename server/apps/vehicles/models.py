from django.db import models



class Vehicle(models.Model):
    vin = models.CharField(max_length=17, null=False, blank=False, db_index=True)

    # objects = ProfileManager()

    class Meta:
        db_table = 'vehicle'

    def __str__(self):
        return 'vehicle/{}'.format(self.vin)

class VehicleSession(models.Model):
    vehicle = models.ForeignKey(Vehicle, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vehicle_session'

class VehicleSessionMetric(models.Model):
    vehicle_session = models.ForeignKey(VehicleSession)
    metric = models.CharField(max_length=255)
    value = models.DecimalField(null=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'vehicle_session_metric'

    def __str__(self):
        return "{}-{}".format(self.metric, self.value)

