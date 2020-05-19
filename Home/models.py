from django.db import models


class Specialty(models.Model):
    """Специальность"""
    title = models.CharField('Называние', max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField("Описание")
    img = models.ImageField(verbose_name='Изображения', upload_to='Specialty/')
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ('-publish',)

