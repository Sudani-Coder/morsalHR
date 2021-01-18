from django.db import models

class Depart_Location(models.Model):
    class Meta:
        verbose_name_plural = 'Department Location'

    dlocation = models.CharField('Department Location', max_length=200)
    dnumber = models.ForeignKey('department.Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.dnumber + " - " + self.dlocation
