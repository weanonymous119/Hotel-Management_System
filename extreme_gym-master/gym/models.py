from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=50)
    joining_date = models.DateField()


    def __str__(self):
        return self.first_name+" "+self.last_name

class Payment(models.Model):
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    payment_date = models.DateField()


class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=50)
    joining_date = models.DateField()

class DietChart(models.Model):
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    profession = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

class Equipments(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cardio = models.CharField(max_length=100)

class Basic_diet(models.Model):
    breakfast = models.CharField(max_length=100)
    lunch = models.CharField(max_length=100)
    dinner = models.CharField(max_length=100)
    extra = models.CharField(max_length=100)
