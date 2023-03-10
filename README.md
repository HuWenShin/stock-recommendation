# Stock Recommendation System
## What the program does
Builds an optimized stock portfolio by analyzing keywords in news titles. The program selects the target company to buy and buy quantity, then rank the companies by the keywords in  news titles. Each keyword is assigned a score, the higher total score of a company the higher ranking it gets. At last, the buy quantity will be allocated to each company in the industry by ranking.

## How the program works
The first 3 lines of input are three files: the news title file (news_title.txt), the keywords and keyword score file (news_dict.txt) and the companies to buy stock from and their stock categories (company_category.txt). The fourth line of input is formatted as: _the stock category to buy from_, _total buy quantity_, _buy quantity in each round of selection seperated by colons (:)_.

If there is no company in the input category, print NO_MATCH. Otherwise, print the company name and buy quantity for each company by their score ranking. 

### Sample 1
**input:**

    /assisting_data/news_title.txt
    /assisting_data/news_dict.txt
    /assisting_data/company_category.txt
    半導體股,12,4:2:1

**output:**

    日月光購買8張
    聯發科購買3張
    台積電購買1張

### Sample 2
**input:**

    /assisting_data/news_title.txt
    /assisting_data/news_dict.txt
    /assisting_data/company_category.txt
    生技股,35,7:5:3:2:1

**output:**

    葡萄王購買15張
    永信購買10張
    國光生購買6張
    杏輝購買4張
