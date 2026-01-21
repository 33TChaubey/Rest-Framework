from django.db import models

# Create your models here.
class CarSpecs(models.Model):
    car_brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    production_year = models.IntegerField()
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)


    def __str__(self):
        return self.car_brand

    class Meta:
        verbose_name_plural = "CarSpecs"