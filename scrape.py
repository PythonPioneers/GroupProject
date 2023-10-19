# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get and return parsed HTML
def get_soup(url):
    # Docker & Splash option. To run without it, replace with r = requests.get(url)
    headers =  {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                "Accept-Encoding": "gzip, deflate", 
                "Accept-Language": "en-US,en;q=0.9", 
               # "Host": "httpbin.org", 
                "Upgrade-Insecure-Requests": "1", 
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15", 
                "X-Amzn-Trace-Id": "Root=1-65318fb8-05013a416770a22748e023f8"
            }
    # Docker & Splash option. To run without it, replace with r = requests.get(url, headers=headers)
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

# Initialize list to store reviews data later on
reviewlist = []

# Function that sifts through the soup element above, tries to find the tags for the data we want, then appends to the list we initialized
def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
            'product': soup.title.text.replace('Amazon.ca:Customer reviews: ', '').strip(), 
            'date': item.find('span', {'data-hook': 'review-date'}).text.strip(),
            'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass

# Function 3: loop through 1:x many pages, or until the css selector found only on the last page is found (when the next page button is greyed)
for i in range(1, 2):
    #soup = get_soup(f"https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_getr_d_paging_btm_next_{i}?ie=UTF8&amp%3Bamp%3BreviewerType=all_reviews&amp%3Bamp%3BpageNumber=10&pageNumber={i}&sortBy=recent")
    #soup = get_soup(f"https://www.amazon.com/Apple-MacBook-13-inch-256GB-Storage/product-reviews/B08N5M7S6K/ref=cm_cr_arp_d_paging_btm_next_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1")
    soup = get_soup(f"https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&amp;amp;reviewerType=all_reviews&amp;amp;pageNumber={i}")
    #soup = get_soup(f'https://www.amazon.co.uk/product-reviews/B0779B2K8B/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_review&sortBy=recent&pageNumber=1')

    print(f'Getting page: {i}')
    print(soup)
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

# Save results to a dataframe, then export as CSV
df = pd.DataFrame(reviewlist)
df.to_csv(r'sony-headphones.csv', index=False)
print('Fin.')
