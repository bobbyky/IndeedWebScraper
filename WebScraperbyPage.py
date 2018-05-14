from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


# URL linking to indeed.com page containing
# list of jobs
job_list = "https://www.indeed.com/q-engineer-l-San-Diego,-CA-jobs.html"
# list used to store URLs linking to job postings
job_urls = []

# Retrieve contents of job list page from indeed.com
jobs = requests.get(job_list)

# Parse through the page using Python's built-in
# HTML parser
job_soup = BeautifulSoup(jobs.content, "html.parser")

# Find the tags that correspond to
# each job listings' url,
# store the url of the job in job_url and append it
# to the list of job urls
job_tbl = job_soup.find(id = "resultsCol")
for link in job_tbl.find_all('a', attrs = {'class' : 'turnstileLink'}):
    job_url = urljoin(job_list, link.attrs['href'])
    job_urls.append(job_url)


# Iterate through each url in job_urls
# For each job listing, print its title, location, company, and url
for x in range(len(job_urls)):

    # Content of web page retrieved using get() function
    # Stored in variable job_page
    job_page = requests.get(job_urls[x])

    # Parse through the page using Python's built-in
    # HTML parser
    soup = BeautifulSoup(job_page.text, "html.parser")

    # Find the tags that correspond to
    # the job posting's title, location, company, and url.
    # Print each job posting's title, location, company, and url.
    job_title = soup.find(class_='jobtitle').get_text()
    print("Title:", job_title)
    job_location = soup.find(class_='location').get_text()
    print("Location:", job_location)
    job_company = soup.find(class_='company').get_text()
    print("Company:", job_company)
    print("URL:", job_urls[x], "\n")

