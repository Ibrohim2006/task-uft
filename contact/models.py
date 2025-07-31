from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class ContactUsModel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=250),
        description = models.TextField()
    )

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)


class WhyChooseUsModel(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=250)
    )

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)


class ContactModel(models.Model):
    fullname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    company_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return f"{self.fullname}"