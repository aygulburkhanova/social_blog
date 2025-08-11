from django.contrib.auth.models import User
from django.db import models

from app.models import TimeStampMixin


class Folower(TimeStampMixin):
    """"
    Дома написать документ
    """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followees")

    def get_followers(self):
        pass

    def get_followees(self):
        pass

    class Meta:
        unique_together = ("from_user", "to_user")







