import scrapy

#-------------------------------------------------------------------
# Command to run: scrapy runspider amazon_review.py -o reviews.csv |
#-------------------------------------------------------------------

class AmazonReviewSpider(scrapy.Spider):
    name = "amazon_review"
    allowed_domains = ["amazon.in"]
    start_urls = ["https://amazon.in/"]

    def parse(self, response):
        pass

class AmazonReviewsSpider(scrapy.Spider):
    name = 'amazon_reviews'
    allowed_domains = ['amazon.in']

    # Define the base URL for the product reviews
    myBaseUrl = "https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_getr_d_paging_btm_next_{next_i}?ie=UTF8&amp%3Bamp%3BreviewerType=all_reviews&amp%3Bamp%3BpageNumber=10&pageNumber={pageNumber}&sortBy=recent"

    def start_requests(self):
        # Start with the first page
        yield scrapy.Request(url=self.myBaseUrl.format(next_i=2, pageNumber=2), callback=self.parse)

    def parse(self, response):
        data = response.css('#cm_cr-review_list')

        # Collecting product star ratings
        star_rating = data.css('.review-rating')

        # Collecting user reviews
        comments = data.css('.review-text')
        count = 0

        # Combining the results
        for review in zip(star_rating, comments):
            stars = ''.join(review[0].xpath('.//text()').extract())
            comment = ''.join(review[1].xpath(".//text()").extract())

            yield {'stars': stars, 'comment': comment}

        # Look for a link to the next page
        next_page_link = response.css('li.next a::attr(href)').extract_first()

        if next_page_link:
            # If there's a link to the next page, extract the 'next_i' value from the URL
            next_i = int(next_page_link.split('next_')[-1].split('?')[0])
            next_page_url = self.myBaseUrl.format(next_i=next_i, pageNumber=next_i)

            # Make a new request for the next page
            yield scrapy.Request(url=next_page_url, callback=self.parse)