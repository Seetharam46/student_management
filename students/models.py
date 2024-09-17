from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    math_marks = models.FloatField()
    science_marks = models.FloatField()
    english_marks = models.FloatField()

    def __str__(self):
        return self.name
