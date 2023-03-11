from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class ContactUs(models.Model):
    full_name = models.CharField(max_length=128)
    subject = models.CharField(max_length=512, )
    content = RichTextField()
    email = models.CharField(max_length=126, null=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.subject