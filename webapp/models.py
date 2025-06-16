from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email} Profile'

class UnitOfMeasure(models.Model):
    name = models.TextField()
    abbreviation = models.TextField()
    metric = models.BooleanField(default=True)
    metric_conversion = models.FloatField(blank=True, null=True)

class State(models.Model):
    name = models.TextField()
    abbreviation = models.TextField()

    def __str__(self):
        return f'{self.abbreviation} - {self.name}'

class Address(models.Model):
    receiver_name = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    line_1 = models.TextField()
    line_2 = models.TextField(blank=True, null=True)
    city = models.TextField()
    postal_code = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    alias = models.TextField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.line_1} {self.city}"

class Client(models.Model):
    name = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Carrier(models.Model):
    name = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=15)
    email = models.EmailField(blank=True, null=True)

class DayOfWeek(models.Model):
    name = models.TextField()
    abbreviation = models.TextField()
    python_day_of_week = models.IntegerField()
    def __str__(self):
        return f'{self.name}'

class ContactType(models.Model):
    name = models.TextField()

class Contact(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

class ContactClient(Contact):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(ContactType, on_delete=models.CASCADE)

class CarrierContact(Contact):
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE)

class DockDay(models.Model):
    day = models.ForeignKey(DayOfWeek, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    note = models.TextField()
    all_day = models.BooleanField(default=False)

class Site(models.Model):
    name = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    dock_days = models.ManyToManyField(DockDay)

class HaulType(models.Model):
    name = models.TextField()

class HaulStatus(models.Model):
    name = models.TextField()

class Haul(models.Model):
    type = models.ForeignKey(HaulType, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pickup = models.ForeignKey(Site, related_name='pickup', on_delete=models.CASCADE)
    destinations = models.ManyToManyField('webapp.HaulDestination', related_name='destinations')
    status = models.ForeignKey(HaulStatus, on_delete=models.CASCADE)
    blind_bidding = models.BooleanField(default=True)
    listing_pickup_name = models.TextField(blank=True, null=True)

class HaulDestination(models.Model):
    haul = models.ForeignKey(Haul, on_delete=models.CASCADE)
    destination = models.ForeignKey(Site, on_delete=models.CASCADE)
    requires_refrigeration = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sequence = models.IntegerField(blank=True, null=True)
    listing_destination_name = models.TextField(blank=True, null=True)

class Sku(models.Model):
    sku = models.TextField()
    description = models.TextField()

class HaulItem(models.Model):
    destination = models.ForeignKey(HaulDestination, on_delete=models.CASCADE)
    description = models.TextField()
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE, blank=True, null=True)
    dimensions_l = models.FloatField(blank=True, null=True)
    dimensions_w = models.FloatField(blank=True, null=True)
    dimensions_h = models.FloatField(blank=True, null=True)
    dimensions_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, related_name='dimensions_uom')
    mass = models.FloatField(blank=True, null=True)
    mass_uom = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE, related_name='mass_uom')

class Bid(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    haul = models.ForeignKey(Haul, on_delete=models.CASCADE)
    contact = models.ForeignKey(CarrierContact, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class BidItem(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    item = models.ForeignKey(HaulItem, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)