from django.db import models
from modules.events.models import Events
from modules.users.models import User


class EventRegisters(models.Model):
    event = models.ForeignKey(
        Events, on_delete=models.CASCADE, related_name="registers"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registers")
    register_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "event")
        db_table = "event_registers"

    def __str__(self):
        return f"{self.user.username} registrado en {self.event.name}"
