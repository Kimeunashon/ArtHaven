from django.db import models
from users.models import Profile
from artwork.models import Artwork
# Create your models here.

class Order(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Profile, related_name='buyer', on_delete=models.CASCADE)
    seller = models.ForeignKey(Profile, related_name='seller', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pending')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} - {self.status}'
