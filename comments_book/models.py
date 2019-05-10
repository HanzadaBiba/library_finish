from django.db import models
from books.models import Books
from django.contrib.auth.models import User
# Create your models here.
class	Comment(models.Model):
    book	=	models.ForeignKey(Books,
                                   on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey(User,related_name='comments_author',on_delete=models.CASCADE)
    body	=	models.TextField(verbose_name='Комментария')
    created	=	models.DateTimeField(auto_now_add=True)
    updated	=	models.DateTimeField(auto_now=True)
    comments_count=models.PositiveIntegerField(default=0)
    active	=	models.BooleanField(default=True)
    class	Meta:
        ordering	=	('created',)
        verbose_name_plural='Коментария'
        verbose_name='Коментария'
    def	__str__(self):
        return	' Коментарий {}'.format(self.book)