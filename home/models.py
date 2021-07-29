from django.db import models
from django.contrib.auth.models import User

UNIT_CHOICES = (
    ('Pcs', 'Pcs'),
    ('Kgs', 'Kgs'),
    ('Gms', 'Gms'),
    ('L', 'L')
)

STATUS = (
    ('Bought', 'Bought'),
    ('Left', 'Left'),
    ('Not-Available', 'Not-Available')
)

class Product(models.Model):
    name = models.CharField(max_length = 300)
    quantity = models.IntegerField()
    unit = models.CharField(max_length = 5, choices = UNIT_CHOICES)
    status = models.CharField(max_length = 150, choices = STATUS)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name