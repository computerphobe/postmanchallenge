from django.db import models

# Create your models here.
class DrugInventory(models.Model):
    drug_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.drug_name

