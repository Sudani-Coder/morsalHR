from django.db import models

class Department(models.Model):
    dnumber = models.AutoField('Department Number', primary_key=True)
    dname = models.CharField('Department Name', max_length=150)
    mgr_ssn = models.ForeignKey("employee.Employee", on_delete=models.CASCADE)
    mgr_start_date = models.DateField()

    def __str__(self):
        return self.dname
