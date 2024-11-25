from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(max_length=50, verbose_name="Email")
    phone_number =models.CharField(max_length=11, verbose_name="Phone Number")

    INSTRUMENT_CHOICES = [
            ('guitar', 'Guitar'),
            ('piano', 'Piano'),
            ('drums', 'Drums'),
            ('violin', 'Violin'),
            ('flute', 'Flute'),
            ('saxophone', 'Saxophone'),
            ('trumpet', 'Trumpet'),
    ]
    
    instrument_type = models.CharField(max_length=200, choices=INSTRUMENT_CHOICES,)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name + " " + self.last_name
