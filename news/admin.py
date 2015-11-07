from django.contrib import admin

from .models import News

# first publishing criteria of an article is its length
# get length shows the length of each article in article list of admin panel
# ready is set by the author of the article to let admin know 
# the article is in the publishable form
# each user has its own article on the same idea
class NewsAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'news_title', 'news_body', 'ready']
	list_display = ('news_title', 'pub_date', 'get_length', 'ready')

admin.site.register(News, NewsAdmin)
