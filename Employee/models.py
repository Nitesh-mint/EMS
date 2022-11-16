from django.db import models

class Employee(models.Model):
    Name = models.CharField(max_length=50,null=False)
    address = models.CharField(max_length=20,null=False)
    date_of_brith = models.DateField(null=False)
    POST_CHOICES = (
        ("PM","Project Manager"),
        ("WD","Web Developer"),
        ("SE","Sotware Engineer"),
        ("AI","Aritificial Intellgence"),
        ("A","Asistant"),
    )
    Post = models.CharField(max_length=50, choices=POST_CHOICES,default="A")
    joined_date = models.DateField(null=False)      

    def __str__(self):
        return self.Name