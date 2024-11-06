from django.db import models
from core.models import SoftDeleteModel
from django.utils import timezone

class Session(SoftDeleteModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    session_datetime = models.DateTimeField()
    session_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email}'s session on {self.session_datetime}"

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        # Soft delete related shots
        self.shot_set.update(is_deleted=True, deleted_at=timezone.now())
        self.save()

class Shot(SoftDeleteModel):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    club = models.ForeignKey('clubs.Club', on_delete=models.PROTECT)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.club} shot: {self.distance} yards"