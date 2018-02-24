# Zomato-User-Data

Scrapes data of zomato users from their profile page. The scraped data will be stored in /zomato_user_data

The data scraped of a user consists of the following fields:-

1. Name

2. Location

3. Number of reviews

4. Number of followers

5. Number of blog posts

6. Count of bookmarks

7. Count of been-there

8. Foodie Level

9. Points to level up

10. Verified/Non-Verified User

11. Number of neighbourhoods he is an expert in, followed by the neighbourhoods.


All the user links which are to be scraped are maintained in "user-links" file.


"Skip_lines" is to maintain iterative scraping, i.e. to continue scraping from the last user scraped in case the code has to be run again.
