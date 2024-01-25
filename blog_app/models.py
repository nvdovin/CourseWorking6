from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.CharField(max_length=100, verbose_name="Slug")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(verbose_name="Превью", upload_to="catalog/media", null=True, blank=True)
    creation_date = models.DateField(auto_now=True, verbose_name="Дата сощдания")
    is_published = models.BooleanField(default=True, verbose_name="Статус публикации")
    views_counter = models.IntegerField(verbose_name="Счетчик просморов", default=0)
    post_author = models.CharField(max_length=50, verbose_name="Автор", null=True, blank=True)

    def __str__(self) -> str:
        return f"Запись {self.title} с количеством просмотров - {self.views_counter}"

    class Meta:
        verbose_name = "Блог для сайта"
        verbose_name_plural = "Блоги для сайта"
