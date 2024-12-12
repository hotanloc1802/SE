from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomerAccount)
admin.site.register(FlowerType)
admin.site.register(Flower)
admin.site.register(FlowerSize)
admin.site.register(FlowerContaining)
admin.site.register(CustomerStyle)
admin.site.register(CustomerStyleFlower)
admin.site.register(CustomerHoliday)
admin.site.register(CustomerHolidayFlower)
admin.site.register(Payment)
admin.site.register(CustomerBill)
admin.site.register(OrderList)
admin.site.register(CustomerOrder)
admin.site.register(CustomerFeedBack)