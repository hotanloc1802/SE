from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomerAccountManager(BaseUserManager):
    def create_user(self, AccountID, AccountName, password=None, **extra_fields):
        if not AccountID:
            raise ValueError('The AccountID must be set')
        user = self.model(AccountID=AccountID, AccountName=AccountName, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, AccountID, AccountName, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(AccountID, AccountName, password, **extra_fields)

class CustomerAccount(AbstractBaseUser, PermissionsMixin):
    AccountID = models.CharField(max_length=255, primary_key=True)
    AccountName = models.CharField(max_length=255, unique=True)
    AccountPassword = models.CharField(max_length=255,default='default_password')
    AccountType = models.CharField(max_length=255)
    CustomerID = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomerAccountManager()

    USERNAME_FIELD = 'AccountName'
    REQUIRED_FIELDS = ['AccountID']

    def __str__(self):
        return self.AccountName


class Customer(models.Model):
    CustomerID = models.CharField(max_length=255, primary_key=True)
    CustomerName = models.CharField(max_length=255)
    CustomerAddress = models.CharField(max_length=255)
    CustomerPhone = models.CharField(max_length=15)
    CustomerAge = models.SmallIntegerField()

    def __str__(self):
        return self.CustomerName

class FlowerType(models.Model):
    FlowerTypeId = models.CharField(max_length=255, primary_key=True)
    FlowerTypeName = models.CharField(max_length=255)

    def __str__(self):
        return self.FlowerTypeName

class Flower(models.Model):
    FlowerId = models.CharField(max_length=255, primary_key=True)
    FlowerName = models.CharField(max_length=255)
    FlowerTypeId = models.ForeignKey(FlowerType, on_delete=models.CASCADE)
    FlowerColor = models.CharField(max_length=100)
    FlowerDescription = models.TextField()
    Image = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.FlowerName

class FlowerSize(models.Model):
    FlowerSizeID = models.CharField(max_length=255, primary_key=True)
    FlowerSizeName = models.CharField(max_length=255)
    NumofFlower = models.IntegerField()

    def __str__(self):
        return self.FlowerSizeName

class FlowerContaining(models.Model):
    FlowerContainingID = models.CharField(max_length=255, primary_key=True)
    FlowerContainingName = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.FlowerContainingName

class CustomerStyle(models.Model):
    CustomerStyleID = models.CharField(max_length=255, primary_key=True)
    CustomerStyleName = models.CharField(max_length=255)

    def __str__(self):
        return self.CustomerStyleName

class CustomerStyleFlower(models.Model):
    CustomerStyleID = models.ForeignKey(CustomerStyle, on_delete=models.CASCADE)
    FlowerID = models.ForeignKey(Flower, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('CustomerStyleID', 'FlowerID')

class CustomerHoliday(models.Model):
    CustomerHolidayID = models.CharField(max_length=255, primary_key=True)
    CustomerHolidayName = models.CharField(max_length=255)
    CustomerHolidayBegin = models.DateField()
    CustomerHolidayEnd = models.DateField()

    def __str__(self):
        return self.CustomerHolidayName

class CustomerHolidayFlower(models.Model):
    CustomerHolidayID = models.ForeignKey(CustomerHoliday, on_delete=models.CASCADE)
    FlowerID = models.ForeignKey(Flower, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('CustomerHolidayID', 'FlowerID')

class Payment(models.Model):
    PaymentID = models.CharField(max_length=255, primary_key=True)
    PaymentName = models.CharField(max_length=255)

    def __str__(self):
        return self.PaymentName

class CustomerBill(models.Model):
    BillID = models.CharField(max_length=255, primary_key=True)
    BillDate = models.DateField()
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Bill {self.BillID} - {self.BillDate}"

class OrderList(models.Model):
    OrderID = models.CharField(max_length=255, primary_key=True)
    FlowerID = models.ForeignKey(Flower, on_delete=models.CASCADE)
    FlowerSizeID = models.ForeignKey(FlowerSize, on_delete=models.CASCADE)
    FlowerContainingID = models.ForeignKey(FlowerContaining, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f"Order {self.OrderID}"

class CustomerOrder(models.Model):
    OrderID = models.ForeignKey(OrderList, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    BillID = models.ForeignKey(CustomerBill, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.OrderID} for {self.CustomerID}"

class CustomerFeedBack(models.Model):
    FeedBackID = models.CharField(max_length=255, primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    FlowerID = models.ForeignKey(Flower, on_delete=models.CASCADE)
    Content = models.TextField()

    def __str__(self):
        return f"Feedback {self.FeedBackID}"

