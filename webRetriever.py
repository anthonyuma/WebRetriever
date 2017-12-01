import urllib2
import sys
from bs4 import BeautifulSoup
# Ditmir Hasani
# script for scraping information on a given url
print "############################### WEB RETRIEVER ###############################"
web_address = raw_input('Please enter a URL : ').strip()
# web_address.strip()
website = str(web_address)
# website.strip()
web_page_load = urllib2.urlopen('https://{}'.format(web_address))
soup = BeautifulSoup(web_page_load,'lxml')
print "-------------------------------------"

def retrieve_info():
	user_choice = int(input("Please select from the following options :  \n [1] Retrieve links from page, \n [2] Raw Page \n"
		" [3] Raw Links \n [4] Return all visible 'p' tags \n [5] Retrieve all text within p tags  \n [9] Exit  \n >>> "))
	if user_choice == 1:
		print "The following links were retrieved from {}".format(web_page_load)
		for links in soup.find_all("a"):
			print "{}".format(links.get("href"))
	elif user_choice == 2:
			print "The Raw page looks like this :{}".format(soup)
	elif user_choice == 3:
		print "Retrieving raw link tags....."
		for rawlinks in soup.find_all("a"):
			print rawlinks
	elif user_choice == 4:
		print "Retrieving all p tags ....."
		for ptags in soup.find_all("p"):
	elif user_choice == 5:
		for ptagtext in soup.find_all("p"):
			print ptagtext.get_text()
	elif user_choice == 9:
		print 'Goodbye !'
		sys.exit()
	elif user_choice != 1 or 2 or 3 or 4 or 5 or 9:
		retry = raw_input("You have not made a valid selection , would you like to rety ? Y/N : " )
		if retry == 'y' or 'Y':
			retrieve_info()
		else:
			print 'Goodbye!'

retrieve_info()
