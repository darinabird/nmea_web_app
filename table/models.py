from django.db import models


class GPSData(models.Model):
    source = models.CharField(
        verbose_name='Источник',
        max_length=10,
    )
    time = models.CharField(
        verbose_name='Время',
        max_length=15,
        blank=True,
    )
    status_valid = models.CharField(
        verbose_name='Статус',
        max_length=1,
        blank=True,
    )
    latitude = models.CharField(
        verbose_name='Широта',
        max_length=30,
        blank=True,
    )
    n_s = models.CharField(
        verbose_name='Для широты',
        max_length=1,
        blank=True,
    )
    longitude = models.CharField(
        verbose_name='Долгота',
        max_length=10,
        blank=True,
    )
    e_w = models.CharField(
        verbose_name='Для долготы',
        max_length=1,
        blank=True,
    )
    speed = models.FloatField(
        verbose_name='Скорость',
        blank=True,
        null=True,
    )
    path_agele = models.CharField(
        verbose_name='Путевой угол',
        max_length=15,
        blank=True,
    )
    date = models.CharField(
        verbose_name='Дата',
        max_length=6,
        blank=True,
    )
    height = models.FloatField(
        verbose_name='Магнитное склонение',
        blank=True,
        null=True,
    )
    direction_magnetic_declination = models.CharField(
        verbose_name='Направление магнитного склонения',
        max_length=1,
        blank=True,
        null=True,
    )
    mode = models.CharField(
        verbose_name='Направление магнитного склонения',
        max_length=1,
        blank=True,
    )
    checksum = models.CharField(
        verbose_name='Направление магнитного склонения',
        max_length=1,
        blank=True,
    )

    class Meta:
        verbose_name = "csv_view_on_web"

    def __str__(self):
        s = '{}. {} {} {}'.format(self.pk, self.source, self.speed, self.height)
        return s
