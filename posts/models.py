from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile

class Post(models.Model):
	content = models.TextField(verbose_name='Содержание')
	image = models.ImageField(upload_to='posts_images/%Y/%m/%d/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=True, verbose_name='Изображение')
	liked = models.ManyToManyField(Profile, blank=True, related_name='likes', verbose_name='Лайки')
	updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменение')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')

	def __str__(self):
		return str(self.content[:20])

	def num_likes(self):
		return self.liked.all().count()

	def num_comments(self):
		return self.comment_set.all().count()

	class Meta:
		ordering = ('-created',)
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

class Comment(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
	body = models.TextField(max_length=300, verbose_name='Комменатрий')
	updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменение')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	def __str__(self):
		return str(self.pk)

	class Meta:
		ordering = ('-created',)
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

LIKE_CHOICES = {
	('Like', 'Like'),
	('Unlike', 'Unlike')
}

class Like(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Пользователь')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
	value = models.CharField(choices=LIKE_CHOICES, max_length=8, verbose_name='Значение')
	updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменение')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	def __str__(self):
		return f"{self.user}-{self.post}-{self.value}"