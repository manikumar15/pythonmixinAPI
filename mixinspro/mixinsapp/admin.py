from django.contrib import admin
from .models import Product
admin.site.site_header = 'Mani Kumar'


class Productadmin(admin.ModelAdmin):
    list_display = ('product_id','product_name','product_price','product_color')
    list_filter = ('product_name',)
    search_fields = ('product_name',)

admin.site.register(Product,Productadmin)