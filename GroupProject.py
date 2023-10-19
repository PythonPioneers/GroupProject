from requests_html import HTMLSession
import pandas as pd

class Reviews:
    def __init__(self, asin):
        self.asin = asin
        self.session = HTMLSession()
        #self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15'}
        self.headers = { 
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
                                "Accept-Encoding": "gzip, deflate, br", 
                                "Accept-Language": "en-US,en;q=0.9", 
                                "Upgrade-Insecure-Requests": "1", 
                                "Referer": "https://www.google.com/",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                            }
        self.url = f'https://www.amazon.co.uk/product-reviews/{self.asin}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_review&sortBy=recent&pageNumber='
        #self.url = f'https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/product-reviews/{self.asin}/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber='

    def pagination(self, page):
        r = self.session.get(self.url + str(page))
        if not r.html.find('div[data-hook="review"]'):
            print(self.url + str(page))
            return False
        return r.html.find('div[data-hook="review"]')

    def parse(self, reviews):
        total = []
        for review in reviews:
            title = review.find('a[data-hook="review-title"]', first=True).text
            rating = review.find('i[data-hook="review-star-rating"] span', first=True).text
            body = review.find('span[data-hook="review-body"] span', first=True).text.replace('\n', '').strip()

            data = {
                'title': title,
                'rating': rating,
                'body': body[:100]
            }
            total.append(data)
        return total

    def dataframe (results):
        # Convert the list of lists of dictionaries into a flat list of dictionaries
        flat_results = [review for page_reviews in results for review in page_reviews]
        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(flat_results)



if __name__ == '__main__':
    products = ['B08N5N1WBH', 'B0779B2K8B']
    results = []
    for product in products:
        amz = Reviews(product)
        for x in range(1,2):
            reviews = amz.pagination(x)
            if reviews is not False:
                results.append(amz.parse(reviews))
                print(product)
            else:
                
                print(f"No reviews found on page {x}")
                break
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['title', 'rating', 'body'])

for product_reviews in results:
    # Flatten the list of dictionaries
    flattened_reviews = [review for review in product_reviews]

    # Create a DataFrame from the flattened reviews
    product_df = pd.DataFrame(flattened_reviews)

# Append the product DataFrame to the master DataFrame
df = pd.concat([df, product_df], ignore_index=True)

# Remove everything before the space in "stars" in the 'title' column
df['title'] = df['title'].str.split(' stars', n=1).str[1]

# Remove " out of 5 stars" and format the numbers
df['rating'] = df['rating'].str.replace(' out of 5 stars', '').str.replace('.0', '')

# Rename the columns and reorder them
df = df.rename(columns={'title': 'Title', 'body': 'Comment', 'rating': 'Rating'})

print(df)