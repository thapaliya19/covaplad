from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("name", "country"), name="unique_name_country"
            ),
        )

    def __str__(self):
        return f"{self.name}, {self.country}"


class District(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("name", "province"), name="unique_name_province"
            ),
        )

    def __str__(self):
        return f"{self.name}, {self.province}"


class Municipality(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    is_rural = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "municipalities"

        constraints = (
            models.UniqueConstraint(
                fields=("name", "district"), name="unique_name_district"
            ),
        )

    def __str__(self):
        return f"{self.name}, {self.district}"


class Ward(models.Model):
    number = models.PositiveSmallIntegerField()
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("number", "municipality"), name="unique_number_municiplaity"
            ),
        )

    def __str__(self):
        mun_name, rest = str(self.municipality).split(",", 1)
        return ",".join((f"{mun_name}-{self.number}", rest))