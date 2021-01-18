from django.db import models

sex = [
    ('M', 'male'),
    ('F', 'female'),
]

class Employee(models.Model):
    ssn = models.AutoField(primary_key=True)
    fname = models.CharField('First Name', max_length=150)
    minit = models.CharField('Middle Name', max_length=150)
    lname = models.CharField('Last Name', max_length=150)
    bdate = models.DateField('birth date')
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=sex, default=1)
    salary = models.FloatField()
    super_ssn = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    dno = models.ForeignKey("department.Department", verbose_name="Department Number", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.fname + self.lname
