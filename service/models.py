from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class OurServicesModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=250),
        name = models.CharField(max_length=250),
        title2 = models.CharField(max_length=250),
        name2 = models.CharField(max_length=250),
        description = models.TextField()
    )
    icon = models.ImageField(upload_to='service/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)




class OurTechnologyModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=250),
        name = models.CharField(max_length=250)
    )
    icon = models.ImageField(upload_to='service/', blank=True, null=True)

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

