#https://www.youtube.com/watch?v=UD4VzOfhBCQ
from requests_html import HTMLSession
import pandas as pd
import os
import csv

class Reviews:
    def __init__(self, asin):
        self.asin = asin
        self.session = HTMLSession()
        self.headers = { 
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
                                "Accept-Encoding": "gzip, deflate, br", 
                                "Accept-Language": "en-US,en;q=0.9", 
                                "Upgrade-Insecure-Requests": "1", 
                                "Referer": "https://www.google.com/",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
                            }
        self.url = f'https://www.amazon.co.uk/product-reviews/{self.asin}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_review&sortBy=recent&pageNumber=1'


    # Create session with respective URL
    def locate(self):
        r = self.session.get(self.url)
        return r.html.find('div[data-hook="review"]')


    # Store title, ratings, and body data into total tuple
    def parse(self, reviews, asin):
        total = []
        for review in reviews:
            title = review.find('a[data-hook="review-title"]', first=True).text
            rating = review.find('i[data-hook="review-star-rating"] span', first=True).text
            body = review.find('span[data-hook="review-body"] span', first=True).text.replace('\n', '').strip()
            data = {'title': title,'rating': rating,'body': body[:100], 'asin_number': asin}
            total.append(data)
        return total
    

# Read the list of products from the CSV file
def read():
    products = []
    with open("Data/asin.csv", 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
             products.append(row[0])
    return products


def format(results):
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
    return df


# Appending more reviews to our dataset to help with modeling
def moreReviews(df):
    # https://www.kaggle.com/datasets/tarkkaanko/amazon?select=amazon_reviews.csv
    path = "Data/more_reviews.csv"
    moreData = pd.read_csv(path)
    moreData = moreData[['overall', 'reviewText']]
    # Add a  column 'Title' with null values
    moreData['Title'] = None
    # Reorder columns to place 'Title' as the first column
    moreData = moreData[['Title'] + [col for col in moreData.columns if col != 'Title']]
    # Rename the columns
    moreData = moreData.rename(columns={'Title': 'Title', 'reviewText': 'Comment', 'overall': 'Rating'})
    # Append moreData to InitialData
    df = df._append(moreData, ignore_index=True)
    # Create a RecordID column for indexing
    N = len(df)
    df['ID'] = range(1, N + 1)
    # Next, rearrange the columns so that "ID" is the first column
    df = df[['ID'] + [col for col in df.columns if col != 'ID']]
    return df


# Write the DataFrame to a CSV file
def toCSV(df):
    path = "Data/reviews.csv"
    # Check if the CSV file already exists
    if os.path.isfile(path):
        # If the file exists, append data to the existing file
        df.to_csv(path, mode='a', header=False, index=False)
    else:
        # If the file doesn't exist, create a new CSV file
        df.to_csv(path, index=False)
    

if __name__ == '__main__':
    # Read csv of asin codes and store them
    asins = read()
    # Used to store title, rating, comment tuples
    results = []
    # Iterate through the product ID's
    for asin in asins:
        # Create class object
        product = Reviews(asin)
        # Locate the review page
        reviews = product.locate()
        # Crawl and store the product reviews
        results.append(product.parse(reviews, asin))
        # Print product ID
        print(asin)
    # Format results into a dataframe
    df = format(results)
    # Append more reviews from Kaggle
    final_df = moreReviews(df)
    # Export results to csv
    toCSV(final_df)