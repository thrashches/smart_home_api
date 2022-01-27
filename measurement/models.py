from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    class Meta:
        verbose_name = 'датчик'
        verbose_name_plural = 'датчики'

    name = models.CharField(max_length=255, verbose_name='название')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='описание(необязательно)')

    def __str__(self):
        return self.name


class Measurement(models.Model):
    class Meta:
        verbose_name = 'показание'
        verbose_name_plural = 'показания'

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='датчик')
    temperature = models.FloatField(verbose_name='температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время измерения')

    def __str__(self):
        return f'{self.created_at}: {self.sensor.name} {self.temperature}'
