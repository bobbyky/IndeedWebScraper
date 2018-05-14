# IndeedWebScraper

Web scraper built in python to scrape indeed job listings to reveal the titles, locations, company names, and urls of job listings on an indeed.com page. Built using requests, BeautifulSoup and Selenium libaries.

**Project: Web Scraper**

**Instructions:**
*Write a web server that scrapes job listings from Indeed and returns the job titles, locations, and company names.* 


**Version 1:** WebScraperbyURL.py

Interpretation: Given a list of URLs linking to job listings from indeed.com, return the job title, location, company name, and url for each listing.

*Input:* 
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/input1.JPG)

*Output:* 
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/output1.JPG)

**Version 2:** WebScraperbyPage.py

Interpretation: Given a URL linking to a page of job listings from indeed.com, create a list of URLs from each job listing. With the list of URLs for each job listing, return the job title, location, company name, and url for each listing.

*Input:* 
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/input2.JPG)

*Output:* ![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/output2a.JPG)
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/output2b.JPG)

Unfortunately, this version of the project produced an output containing information of job listings not present when you visited the given URL of the indeed.com page containing the list of jobs. The information for each job listing produced from the program differed from what was displayed when you visited the URL from your local device.

*Expected Output:*
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/output2c.JPG)

**Final Version:** WebScraper.py

Interpretation: Given a URL linking to a page of job listings from indeed.com, create a list of URLs from each job listing. With the list of URLs for each job listing, return the job title, location, company name, and url for each listing.

To solve the error present in version 2, I used webdriver from the Selenium library as a platform to automate the launching of a chrome web browser to automate the process of web scraping. This fixed the error present in version 2 as the output information for each job listing matched up with the information displayed on the browser.

*Input:*
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/input3.JPG)

*Output:*

![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/output3a.JPG)
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/output3b.JPG)
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/output3c.JPG)
![My image](https://github.com/bobbyky/IndeedWebScraper/blob/master/Images/output3d.JPG)



