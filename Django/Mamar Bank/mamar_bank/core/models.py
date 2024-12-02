from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    reserve_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk and Bank.objects.exists():
            raise ValueError("Only one Bank instance is allowed.")
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        instance, created = cls.objects.get_or_create(
            id=1,  
            defaults={
                "name": "Default Bank Name",
                "address": "Default Address",
                "reserve_balance": 100000000.00,
                "contact_email": "default@bank.com",
                "contact_phone": "+0000000000",
            },
        )
        return instance

    def __str__(self):
        return self.name
