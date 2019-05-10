from django.db import models
from django.urls import reverse
# Create your models here.
class Base(models.Model):
    name=models.CharField(max_length=255,verbose_name='Название')
    slug=models.SlugField(max_length=255,verbose_name='Слаг')
    def __str__(self):
        return self.name
    class Meta:
        abstract=True
class Author(Base):

    def get_absolute_url(self):
        return reverse('home:author_detail',args=[self.slug])
    class Meta:
        verbose_name='Авторы'
        verbose_name_plural='Авторы'
class Genre(Base):
    def get_absolute_url(self):
        return reverse('home:genre_detail',args=[self.slug])
    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанр'
class Books(Base):
    description=models.TextField(verbose_name='Описание')
    author=models.ForeignKey(Author,verbose_name="Автор",on_delete=models.PROTECT,related_name='author_book')
    genre=models.ForeignKey(Genre,verbose_name="Жанр",on_delete=models.PROTECT,related_name='genre_book')
    image=models.ImageField(upload_to='images/%Y/%m/%d',verbose_name='Картина')
    file=models.FileField(upload_to='file/%Y/%m/%d',verbose_name='Книга')
    size=models.CharField(verbose_name='Размер файла',max_length=255,blank=True)
    date=models.DateField(verbose_name='Дата',auto_now_add=True)
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.size:
            self.size=self.file.size
        super(Books, self).save()
    def get_absolute_url(self):
        return reverse('home:book_detail',args=[self.slug])
    class Meta:
        verbose_name_plural='Книги'
        verbose_name='Книги'
        ordering=['date']
