from django.db import models
from users.models import Profile
from artwork.models import Artwork
# Create your models here.

class Comment(models.Model):
    content = models.TextField()
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.created_by.user.username}'
