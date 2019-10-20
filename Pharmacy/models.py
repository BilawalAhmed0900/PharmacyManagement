from django.db import models


class Medicine(models.Model):
    medicine_types = (
        ('O', 'Oral'), ('I', 'IV')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField("Medicine Name", max_length=512)
    manufacturer = models.CharField("Medicine Manufacturer", max_length=128)
    supplier = models.CharField("Medicine Supplier", max_length=128)
    stock = models.IntegerField("Medicine Stock")
    purchase_price = models.IntegerField("Medicine Purchase Price")
    retail_price = models.IntegerField("Medicine Retail Price")
    medicine_type = models.CharField(max_length=1, choices=medicine_types)
