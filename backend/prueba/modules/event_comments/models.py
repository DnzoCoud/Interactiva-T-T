from django.db import models
from modules.events.models import Events
from modules.users.models import User


class Comments(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "event_comments"

    def __str__(self):
        return f"Comentario de {self.user.username} en {self.event.name}"
