# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

def get_name(self):
    return '{} {}'.format(self.first_name, self.last_name)

User.add_to_class("__str__", get_name)

# Create your models here.
class Facility(models.Model):
    name = models.CharField(max_length=200, help_text='Name must be a maximum of 100 characters', unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "4. Facilities"

    def __str__(self):
        return '%s' % (self.name)

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=150, help_text='Name must be a maximum of 150 characters', unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(max_length=4000, help_text='Description must be a maximum of 4000 characters')
    image1 = models.ImageField(upload_to='images/', max_length=254)
    image2 = models.ImageField(null=True, blank=True, upload_to='images/', max_length=254)
    image3 = models.ImageField(null=True, blank=True, upload_to='images/', max_length=254)
    image4 = models.ImageField(null=True, blank=True, upload_to='images/', max_length=254)
    image5 = models.ImageField(null=True, blank=True, upload_to='images/', max_length=254)
    brochure = models.FileField(null=True, blank=True, upload_to='documents/', max_length=254) 
    facilities = models.ManyToManyField(Facility, through='Property_Facility')
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Property"
        verbose_name_plural = "1. Properties"

    def __str__(self):
        return '%s' % (self.name)


class Property_Facility(models.Model):
    property = models.ForeignKey(Property, related_name='+', on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, related_name='+', on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = "5. Property Facilities"

    def __str__(self):
        return '{} {} - {}'.format(self.property.name, 'bedroom', self.facility.name)


class Room_Type(models.Model):
    capacity = models.PositiveSmallIntegerField()
    property = models.ForeignKey(Property, related_name='room_types', on_delete=models.CASCADE)
    price_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    image1 = models.ImageField(null=True, blank=True, upload_to='images/', max_length=254)

    class Meta:
        ordering = ["capacity"]
        verbose_name = "Room-Type"
        verbose_name_plural = "2. Room Types"
        constraints=[
            models.UniqueConstraint(name='unique_room_types',fields=['capacity', 'property'])
        ]

    def __str__(self):
        return '{} bedroom - {} Property '.format(self.capacity, self.property.name)


class Apartment(models.Model):
    room_type = models.ForeignKey(Room_Type, related_name='apartments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text='Name must be a maximum of 50 characters', unique=True)
    STATUS = (
        ('Available', 'Available'),
        ('Booked', 'Booked')
    )
    status = models.CharField(max_length=20, choices=STATUS, default="Available")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "3. Apartments"

    def __str__(self):
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, related_name='reservations', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=30)
    DURATION_TYPE = (
        ('Day', 'Day'),
        ('Week', 'Week'),
        ('Month', 'Month'),
        ('Year', 'Year')
    )
    duration_type = models.CharField(max_length=30, choices=DURATION_TYPE)
    duration = models.PositiveSmallIntegerField(help_text='Example. 2 Years')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid = models.DecimalField(blank=True, default=0, max_digits=10, decimal_places=2)
    STATUS = (
        ('Paid', 'Paid'),
        ('No Payment', 'No Payment')
    )
    first_payment = models.CharField(max_length=15, choices=STATUS, default="No Payment")
    # made_payment = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "6. Reservations"

    def __str__(self):
        return '{}'.format(self.apartment)
       

class Payment(models.Model):
    user = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, related_name='payments', on_delete=models.CASCADE)
    # status = models.CharField(max_length=50, default='Pending', blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_time"]
        verbose_name_plural="7. Payments"

class Blog(models.Model):
    user = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, help_text="Title must be max 100 characters", unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image1 = models.ImageField(upload_to='images/', max_length=254)
    content = models.TextField(max_length=5000, help_text='Content must be a maximum of 5000 characters')
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_time"]
        verbose_name_plural="8. Blogs"