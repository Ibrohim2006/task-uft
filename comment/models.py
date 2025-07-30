from django.db import models
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.

class Comment(TranslatableModel):
    translations = TranslatedFields(
        first_name = models.CharField(max_length=30),
        last_name = models.CharField(max_length=30),
        job = models.CharField(max_length=100),
        company = models.CharField(max_length=100, blank=True, null=True),
        comment = models.TextField()
    )
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    feedback_file = models.FileField(upload_to='feedback_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job}"