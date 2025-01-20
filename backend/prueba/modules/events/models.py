from django.db import models


class Events(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    imagen = models.ImageField(upload_to="eventos/imagenes/")
    capacity = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    ubication = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def available_quotas(self):
        return self.capacity - self.registros.count()
