from requests_html import HTMLSession
import pandas as pd
import os

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
        #self.url = f'https://www.amazon.com/product-reviews/{self.asin}/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber='
        #https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/dp/B08N5KWB9H/ref=sr_1_2?crid=PLUK0XNJ8ZJ2&keywords=macbook&qid=1697802682&sprefix=macbook%2Caps%2C148&sr=8-2

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
    products = ['B08N5N1WBH', 'B0779B2K8B', 'B091G31KSJ', 'B09QXMZHV8', 'B08HLGKP9J', 'B003VQZC3U', 'B08DGPKWWR', 'B08C1RR8JM', 'B01FSGVN4M', 'B00552K0GM', 
                'B0BQNBM2N8', 'B00BSYR7K8', 'B0002M6CW6', 'B08GS8PGSB', 'B00B0KJ3F2', 'B08CVSDS63', 'B09D15SFMQ', 'B01JS6YLQK','B09X7DNF6G', 'B076ZQQTYR', 
                'B000BNSYHW', 'B0751G5NJN', 'B0002E1G5C', 'B08P68RPC1', 'B08FB994L8', 'B08B8XQG8B', 'B095SYWNHJ', 'B08WJSJT4J', '0141976144', 'B08B8XQG8B',
                'B08FB994L8', 'B09S79RJN2', '0786966114', 'B08RZ9VFWB', 'B07TY15FZN', 'B0BDJ37NF5', 'B082FRV6F6', 'B09B2WG9X9', 'B09GPWQYTL', 'B07YV97FHP',
                'B07L8MHVFK', 'B09H3627RB', 'B07W6ZWW7B', 'B07HJ615V9', 'B088TT3QW2', 'B08HZFDQYC', 'B081FPG5QB', 'B09BXQ4HMB', 'B083F23Y7G', '0786966114',
                'B09BNTZH9C', 'B08HRWSYH6', 'B0891YV252', 'B09BK9R4WG', 'B088KVJBQZ', 'B09YL1R3D3', 'B08TK2WHTM', 'B09SWTJZH6', 'B09FKGJ1CB', 'B087GS3ZS7',
                'B09GRL544S', 'B09KM4H1VL', 'B086TKTQ5J', 'B096MJ9LYK', 'B09ZY9N6PD', 'B08SVXG1XY', 'B0913B83M2', 'B08JTXR6YB', 'B083ZY3KFK', 'B07PMLV99S',
                'B096HBQ7Y8', 'B08LTZ7GT1', 'B08CVGQZ6P', 'B07R3FRRLG', 'B08YNTMC49', 'B0883N3R7S', 'B0936FGLQS', 'B08RJ59H6T', 'B09WMV9MQK', 'B07DDN4PYD',
                'B0943DGDNZ', 'B09Q3LN9DQ', 'B095X8QT9P', 'B07VVDS67L', 'B09F65P34Y', 'B08FXBPMR7', 'B0824B1VZB', 'B08B5V3WSK', 'B097S57YDF', 'B07YF8YP5G',
                'B09MG6KK9W', 'B0865JJLHD', 'B082DLNR49', 'B0839TS2VN', 'B07P5PQN7S', 'B0B5HNFPV1', 'B08T7NHP7N', 'B093F8LKVY', 'B08DKBS2NZ', 'B093KD3T3B']
    
    #Will not allow me to mine any more products
    
    #['B0922V5VFP', 'B08VNPVFWW', 'B00J1XE1T8', 'B00QUXM8OC', 'B0964PSHGK', 'B071RDX53D', 'B091MMGTF1', 'B07RQLGSN3', 'B0007W5S8U', 'B07PWTKPTK']

    #products = ['B00GSP5D94']
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

# Write the DataFrame to a CSV file
path = "/Users/mattmacrides/OneDrive - University of Illinois - Urbana/CS 410 - Text Information Systems/GroupProject/data.csv"
# Check if the CSV file already exists
if os.path.isfile(path):
    # If the file exists, append data to the existing file
    df.to_csv(path, mode='a', header=False, index=False)
else:
    # If the file doesn't exist, create a new CSV file
    df.to_csv(path, index=False)