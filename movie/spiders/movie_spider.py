import scrapy
import re 
from movie.items import MovieItem 

class MovieSpider(scrapy.Spider):
    name = "movie"

    file_path=r"/home/wsh/spider/movie/movie/spiders/allMoviesUrl.txt"
    urlList=[]
    urlsFile=open(file_path)
    for url in urlsFile:
        urlList.append(url)
    urlsFile.close()

    start_urls = urlList
	
    def getAllUrls(self):
	file_path=r"allMoviesUrl.txt"
	urlList=[]
	urlsFile=open(file_path)
	for url in urlsFile:
		urlList.append(url)
	urlsFile.close()
	return urlList


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
    
