from django.db import models

# Create your models here.

class Session(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    session_datetime = models.DateTimeField()
    session_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s session on {self.session_datetime}"

class Shot(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    club = models.ForeignKey('clubs.Club', on_delete=models.PROTECT)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"{self.club} shot: {self.distance} yards"