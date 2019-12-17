# importing scrapy package
import scrapy
from ..items import QuotetutorialItem


# class name QuoteSpider where we are inheriting properties from scrapy and Spider
# The name and start_url named must be same as the inhertience parent expect us to
# have the two variables
class QuoteSpider(scrapy.Spider):
	name='quotes'
	start_urls=['http://quotes.toscrape.com/']
    # the quote is stored in variable named all_div_quotes
	def parse(self,response):

		items=QuotetutorialItem()
		all_div_quotes=response.css('div.quote')
		# the quotes extracted will be shown one by one using for loop


		for quotes in all_div_quotes:
    
			#title will store quote and author will store author name and tag will be store tag of quote
		    title=quotes.css('span.text::text').extract()
		    author=quotes.css('.author::text').extract()
		    tag=quotes.css('.tag::text').extract()
		    # the data will be stored in the form of dictionary
		    items ['title']=title
		    items['author']=author
		    items['tag']=tag
		    yield items

		# getting the next page button detail
		next_page=response.css('li.next a::attr(href)').get()

		# if the next page is not null then it goes to the next page 
		if next_page is not None:
			# two optins executed one is the next page and callback decides the execution of the next page executed
			yield response.follow(next_page,callback=parse)





