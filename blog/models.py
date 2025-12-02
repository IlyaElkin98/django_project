from django.db import models

class Blog(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок',
        help_text='Введите заголовок',
    )

    content = models.TextField(
        verbose_name='Содержание',
        help_text='Введите Содержание'
    )

    image = models.ImageField(
        upload_to='blog/photo',
        verbose_name='Изображение',
        help_text = 'Загрузите изображение',
    )

    date_of_creation = models.DateField(
        verbose_name='Дата создания',
        null=True,
        blank=True,
        auto_now_add=True

    )

    publication_sign = models.BooleanField(
        default=True,
    )

    views_counter = models.PositiveIntegerField(
        verbose_name='Счётчик просмотров',
        help_text='Укажите количество просмотров',
        default=0
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

