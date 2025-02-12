from django.core.exceptions import ValidationError
from django.db import models

from addresses.models import Address


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Meter(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    serial_num = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f'{self.category}/"{self.type}"/{self.serial_num}'

    def clean_serial_num(self):
        serial_num = self.cleaned_data.get("serial_num")
        if Meter.objects.filter(serial_num=serial_num).exists():
            raise ValidationError(
                "Счетчик с этим серийным номером уже зарегистрирован."
            )
        return serial_num


class MeterData(models.Model):
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    data = models.PositiveIntegerField(unique=False)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.meter}: {self.data}"
