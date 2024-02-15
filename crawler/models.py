from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Title')
    link = models.URLField(max_length=255, null=False, default='https://www.goodreads.com/',
                           blank=False, verbose_name='Link')
    author = models.CharField(max_length=255, null=False, blank=False, verbose_name='Autor')
    rating = models.CharField(max_length=255, null=False, blank=False, verbose_name='Rating')
    description = models.TextField(null=False, blank=False, verbose_name='Description')

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ('id',)

    def __str__(self):
        return self.title
