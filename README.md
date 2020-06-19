<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Data Thieves
Comparing GoodReads, Amazon and NYTimes
# Description
Comparing Bestseller lists, by analyzing how the ranking system functions. GoodReads review system, Amazon copies sold, NYTimes publisher copies sold. The point is to see how books receive their bestseller position and what common themes were see in all three sources. 

# Organization
We knew what sources we wanted to scrape. Considering the sources and the information we could obtain we could do a limited comparison.
NYTimes provides only one value which is a book place and 3 books that are in the 2 other websites.
Amazon has reviews, book place (rank of the most sold, like NYTimes) and also number of reviews.
Goodreads has a horde of reviews, rankings, number of readers, number of reviewers. An abundance of values to compare to the other two queries.

After scraping, we needed to figure out what information was in common. Some books were in the all 3 of the lists. 
We could obtain avarege reviews from the 2 of the lists.
Compare the number of reviewers.
After that dropping all of the irrelevant information
Creating a central data point.

For fun, we tried to figure out how to make it a product, based on a real example and who would be interested in it.

# Project structure
- Assets: holds one raw dataset csv file.
- Data: all clean data each scraped site is in its own csv file.  
- Notebooks: work of each person, not cleaned, just the scrape everybody conducted.
- Utility: queries and organizing of the datasets
- Magic Baby Maker: is the main list generator. It draws functions from the utility folder.

# Project status
Regina - crying
Edgar - saveing the day
Cezar - on point
# Resources
https://www.amazon.com/best-sellers-books-Amazon/zgbs/books
https://www.goodreads.com/book/most_read?category=all&country=all&duration=m
https://www.nytimes.com/books/best-sellers/2020/06/21/

# Files
Presentation: https://docs.google.com/presentation/d/1N5oR24kfeKP52GXrmN-7UDie04WAIvVRj4er0nQhvN8/edit?usp=sharing
Trello: https://trello.com/b/gjac24Ec/shark-data-project