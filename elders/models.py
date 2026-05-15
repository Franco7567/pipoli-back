from django.db import models

from django.db import models
from users.models import User


class Elder(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    birth_date = models.DateField()

    address = models.TextField()

    medical_notes = models.TextField(
        blank=True,
        null=True
    )

    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='elders'
    )

    caregivers = models.ManyToManyField(
        User,
        related_name='assigned_elders',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
