from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Portfolio(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        description=models.TextField(),
    )
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
