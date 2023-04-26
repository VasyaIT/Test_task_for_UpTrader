from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='menu title', help_text='Enter the name of menu')
    slug = models.SlugField(max_length=255, verbose_name="menu slug", db_index=True, help_text='URL')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.CharField(max_length=255, verbose_name='subject title', help_text='Enter the name of Subject')
    slug = models.SlugField(max_length=255, verbose_name="subject slug", help_text='URL')
    menu = models.ForeignKey(Menu, blank=True, related_name='subjects', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Menu subject'
        verbose_name_plural = 'Menu subjects'

    def __str__(self):
        return self.title
