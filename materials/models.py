from django.db import models


# Create your models here.



class Etablissement(models.Model):
    name = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Hardware(models.Model):
    CONDITION_CHOICES = (
        ('bad', 'bad'),
        ('ok', 'ok'),
        ('new', 'new'),
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="parc")
    price = models.IntegerField(help_text="Prix d'achat HT en CHF")
    buy_date = models.DateTimeField(verbose_name="Date d'achat", help_text="Ou date de mise en service")
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=200)
    is_deleted = models.BooleanField(default=False)
    etablissement = models.ForeignKey(Etablissement, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{category} acheté en {year}".format(category=self.category, year=self.buy_date.year)

    class Meta:
        ordering = ("buy_date",)
