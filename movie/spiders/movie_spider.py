import scrapy
import re 
from movie.items import MovieItem 

class MovieSpider(scrapy.Spider):
    name = "movie"
    start_urls = [
        'http://www.imdb.com/title/tt0114746/',
        'http://www.imdb.com/title/tt0137523/',
    ]

    def parse(self, response):
    	title=response.xpath('//meta[@property="og:title"]/@content').extract()[0]
	poster=response.xpath('//meta[@property="og:image"]/@content').extract()[0]
	url=response.url
	movie_id=re.search('\d{7}',url).group()
	print movie_id
	print title
	print url
	print poster

	item = MovieItem()  
        
	item["movie_poster"]=poster
	item["movie_id"]=movie_id
	item["movie_name"]=title
	item["movie_url"]=url

	return item
