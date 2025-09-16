from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_count = models.PositiveBigIntegerField(default=0)

    def get_discount_price(self, discount_percentage):
        return self.price * (1 - discount_percentage / 100)

    @property
    def in_stock(self) -> bool:
        return self.stock_count > 0

    def clean(self):
        if self.price < 0:
            raise ValidationError('price can not be negative')
        
        if self.stock_count < 0:
            raise ValidationError('stock cound can not be negative')
        
