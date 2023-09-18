from django.db import models
from django.utils.text import slugify  # allows all str w/ spaces tunr into URL friendly with - dashes


# Create your models here.
# Create a model to save shortened links - name, url, slug, # of clicks

class Link(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)

    # this dunder method allows to view on the admin what is what(links) more clearly
    # Instead of link object (1) ---> its link {name}
    def __str__(self):
        return f'{self.name} | {self.clicks}'

    # Create a method to apply to the class, this method will allow the clicks to increment each time instead of
    # manually doing it
    def click(self):
        self.clicks += 1  # increments by one, and save it
        self.save()

    # Set-up slug field so it works automatically(import slugify)
    # Here checking if somebody entered a slug, IF NOT it automatically creates one from the name
    def save(self, *args, **kwargs):
        if not self.slug:  # if no slug then....
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)  # this will continue to save with new slug name
