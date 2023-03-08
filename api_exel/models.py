from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.FileField(upload_to='img', null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'MyModel'
        verbose_name_plural = 'MyModels'
