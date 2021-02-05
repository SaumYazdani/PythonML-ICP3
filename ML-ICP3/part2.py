#importing libraries
import requests
from bs4 import BeautifulSoup
#list of links to be used later
links = []
#setting website variable = to the webpage request
website = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
#using beautiful soup to parse the webpage content
soup = BeautifulSoup(website.content,"html.parser")
#printing the title of the webpage
print (soup.title.string)
print ('-----------------------------------------------------------------------------------------')
#separating all the a attributes, then looking for all the href tags and appending the href results to links list
for link in soup.find_all('a'):
    links.append(link.get('href'))
#printing each element (link) in the links list
for i in range(len(links)):
    print ((links[i]))
