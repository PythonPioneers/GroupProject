# https://martinctc.github.io/blog/vignette-scraping-amazon-reviews-in-r/

library(tidyverse)
library(rvest)
scrape_amazon <- function(ASIN, page_num){
  
  url_reviews <- paste0("https://www.amazon.co.uk/product-reviews/",ASIN,"/?pageNumber=",page_num)
  
  doc <- read_html(url_reviews) # Assign results to `doc`
  
  # Review Title
  doc %>% 
    html_nodes("[class='a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold']") %>%
    html_text() -> review_title
  
  # Review Text
  doc %>% 
    html_nodes("[class='a-size-base review-text review-text-content']") %>%
    html_text() -> review_text
  
  # Number of stars in review
  doc %>%
    html_nodes("[data-hook='review-star-rating']") %>%
    html_text() -> review_star
  
  # Return a tibble
  tibble(review_title,
         review_text,
         review_star,
         page = page_num) %>% return()
}


asin_list <- read_csv("/Users/ethanshen/Documents/UIUC/Fa23/CS410/GroupProject/asin.csv")
review_df <- tibble()
for (i in 1:length(asin_list$Product)) {
  print(asin_list$Product[i])
  tryCatch({
    temp <- scrape_amazon(ASIN = asin_list$Product[i], page_num = 1)
    temp$asin <- asin_list$Product[i]
    review_df <- bind_rows(review_df, temp)
    Sys.sleep(3)
    message("Taking a break...") 
    
    if((i %% 15) == 0){
      
      message("Taking a 60 sec break...")
      
      Sys.sleep(60)
    }
  }, 
  error = function(e) {})
}

review_df_final <- review_df %>% 
  mutate(review_title = review_title %>% str_replace_all("\n","") %>% str_trim(),
         review_text = review_text %>% str_replace_all("\n","") %>% str_trim(),
         rating = substr(review_star, 1, 3) %>% as.integer()) %>% 
  separate(review_title, into = c('num_stars', 'title'), sep = '        ')

review_df_final %>% write_csv("/Users/ethanshen/Documents/UIUC/Fa23/CS410/GroupProject/reviews_ethantest.csv")

