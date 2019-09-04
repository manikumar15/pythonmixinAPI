from django.db import models

class Product(models.Model):
	product_id=models.IntegerField(primary_key=True)
	product_name=models.CharField(max_length=20)
	product_price=models.FloatField()
	product_color=models.CharField(max_length=20)

	def __str__(self):
		return self.product_name

