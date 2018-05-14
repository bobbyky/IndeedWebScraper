from bs4 import BeautifulSoup
import requests


# list of urls linking to job listings
urls = ["http://www.indeed.com/viewjob?jk=8cfd54301d909668",
        "http://www.indeed.com/viewjob?jk=b17c354e3cabe4f1",
        "http://www.indeed.com/viewjob?jk=38123d02e67210d9"]

# Iterates through each url in the list
# For each job listing, print its title, location, company, and url
for x in range(len(urls)):

    # Content of web page retrieved using get() function
    # Stored in variable page
    page = requests.get(urls[x])

    # Parse through the page using Python's built-in
    # HTML parser
    soup = BeautifulSoup(page.text, "html.parser")

    # Find the tags that correspond to
    # the job posting's title, location, company, and url.
    # Print each job posting's title, location, company, and url.
    job_title = soup.find(class_='jobtitle').get_text()
    print("Title:", job_title)
    job_location = soup.find(class_='location').get_text()
    print("Location:", job_location)
    job_company = soup.find(class_='company').get_text()
    print("Company:", job_company)
    print("URL:", urls[x], "\n")
