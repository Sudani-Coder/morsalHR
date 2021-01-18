from django.db import models

class Project(models.Model):
    pnumber = models.AutoField('Project Number', primary_key=True)
    pname = models.CharField('Project Name', max_length=150)
    plocation = models.CharField('Project Location', max_length=200)
    dnumber = models.ForeignKey('department.Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.pname
