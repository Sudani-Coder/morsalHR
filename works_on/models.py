from django.db import models

class works_on(models.Model):
    Pno   = models.ForeignKey("project.Project", verbose_name="Project Number",on_delete=models.CASCADE)
    Essn  = models.ForeignKey("employee.Employee", on_delete=models.CASCADE)
    Hours = models.CharField(max_length=200)

    def __str__(self):
        return self.Pno + " - " + self.Essn
