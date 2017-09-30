from django.db import models


class State(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'state'

    def __str__(self):
        return self.code


class Zipcode(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    city = models.CharField(max_length=255)
    state = models.ForeignKey(State, db_column='state', null=False, blank=False)

    class Meta:
        db_table = 'zipcode'
        ordering = ['code']

    def __str__(self):
        return self.code
