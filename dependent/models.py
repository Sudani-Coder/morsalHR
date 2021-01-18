from django.db import models

sex = [
    ('M', 'male'),
    ('F', 'female'),
]

class Dependent(models.Model):
    Essn = models.ForeignKey("employee.Employee", on_delete=models.CASCADE)
    Dependent_name  =  models.CharField("Dependent Name", primary_key=True, max_length=250)
    gender = models.CharField(max_length=10, choices=sex, default=1)
    Relationship =  models.CharField(max_length=250)
    bdate = models.DateField('birth date')

    def __str__(self):
        return self.Dependent_name
