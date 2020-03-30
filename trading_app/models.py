from django.db import models

# Create your models here.
class todays(models.Model):
    Comany_symbol = models.CharField(max_length=64)
    company_name = models.CharField(max_length=64)
    price_data = models.CharField(max_length=64)
    change = models.CharField(max_length=64)
    change_in_percentage =  models.CharField(max_length=64)
    volume = models.CharField(max_length=64)
    Avgvol_In3Month = models.CharField(max_length=64)
    Market_cap = models.CharField(max_length=64)
    PE_ratio = models.CharField(max_length=64)

    def __str__(self):
        return self.company_name