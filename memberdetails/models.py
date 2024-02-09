from django.db import models

# Create your models here.


class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('W', 'Widowed'),
        ('D', 'Divorced'),
    ]

    member_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField()
    home_phone = models.CharField(max_length=20, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    post_code = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    emergency_contacts = models.TextField(blank=True, null=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.full_name} ({self.member_id})"
