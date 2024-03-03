from django.db import models

class UserDetails(models.Model):
    GENDER_CHOICES = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    ]

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email_id = models.EmailField(null=False, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=False)
    current_address = models.CharField(max_length=255, null=False)
    permanent_address = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    user_type = models.CharField(max_length=255, null=False)
    user_role = models.CharField(max_length=255, default=None, null=True, blank=True)
    additional_information = models.JSONField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    
    class Meta:
        managed = False
        db_table = 'user_details'