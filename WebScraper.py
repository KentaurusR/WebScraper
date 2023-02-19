import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import validators

url = input("Hi, please enter the URL of a website to scrape: ")

# Create a list that will be appended with each link in the website
link_list = []

# Validate the URL to make sure that the user provides a valid link
while True:
    if not validators.url(url):
        url = input("Invalid URL detected, make sure it is formatted correctly - please provide a real website URL: ")
    else:
        break

print("Thank you, we will now scrape all of the links from this webpage containing an '<a>' tag and print them for you.")


# Make a GET request to fetch the webpage content
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

print("Here are all of the links I could scrape on this page: ")

# Using a for loop and the .find_all method in BeautifulSoup, we are going to find all links
# We use "a" as the argument in soup.find_all because the "a" tag is an HTML element that is used to create hyperlinks
# This allows us to find the "href" attribute of each "a" tag, which contains the URL that the link points to
# "href" stands for 'hypertext reference'

for link in soup.find_all("a"):
    href = link.get("href")
    # Our 'link.get("href")' method might return 'None' for elements that don't have an "href" attribute, we don't want to print these
    if href is not None:
        # It is common to receive links that are not full URLs, but rather relative links or fragments that are intended to be combined with the base URLs
        # These aren't clickable for our user, so we want to convert these links into full URLs
        # We use href.startswith to check for href values that don't start with 'https'
        # Then, we use urljoin from the urllib.parse module to join these with the URL provided by the user
        if not href.startswith("https"):
            href = urljoin(url, href)
        link_list.append(href)

for i in link_list:
    print(i)

if link_list == []:
    print("That's strange, I couldn't scrape any links from this webpage.")
else:
    print("\nThank you for using my web scraper, have a nice day!")