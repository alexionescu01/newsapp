from django.db import models

class News(models.Model):
	news_title = models.CharField(max_length=100)
	news_body = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date_published')
	ready = models.BooleanField()
	news_length = models.IntegerField(default=0)

	def get_length(self):
		return len(self.news_body)

	class Meta:
		verbose_name_plural = 'news'
