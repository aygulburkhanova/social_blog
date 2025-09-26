from django.contrib.auth.models import User
from django.db import models

from app.models import TimeStampMixin


class Follower(TimeStampMixin):
    """

    """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="followees")

    class Meta:
        unique_together = ("from_user", "to_user")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.CharField(max_length=1024, null=True, blank=True)