from django.db import models

# Create your models here.
class DummyTable(models.Model):
    dummy_field_name = models.TextField()

    def __str__(self) -> str:
        return f"{self.dummy_field_name}"
    
