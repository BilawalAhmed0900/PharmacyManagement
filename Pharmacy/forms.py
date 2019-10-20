from django import forms


class MedicineForm(forms.Form):
    medicine_name = forms.CharField(label="medicine_name", max_length=512)
    retail_price = forms.IntegerField(label="retail_price")
    medicine_type = forms.CharField(label="medicine_type", max_length=1)
