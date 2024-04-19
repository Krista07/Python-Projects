#I made this script about 2 years ago when I wanted to learn more about web scrapping.
#This code is a simple and basic web scrapper for a website called Newegg.

#If you decide to copy this code and run it on other websites, please keep in mind there are laws and regulations regarding web scrapping.
#Please review you local and state laws before deciding to do so.

#Newegg is okay with their website being scrapped, as along as you are not spamming the request. Otherwise, they may ban you IP address.

#Web Scraper Project
#This web scraper project finds the price of an item on Newegg. 

#import using BeautifulSoup4
from bs4 import BeautifulSoup
import requests

#This is a link to a specific item on Newegg. I wanted to know the price of said item without having to go to the website directly.

#Must use http or https only, otherwise you'll get an error.
url = "https://www.newegg.com/sandisk-1tb-microsdxc/p/N82E16820173498?Description=micro%20ssd&cm_re=micro_ssd-_-20-173-498-_-Product&quicklink=true"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

#Finds the information from the $ sign within the HTML script
prices = doc.find_all(string="$")

#Finding the parent tag in the html file from the website
parent = prices[0].parent

#For some reason Newegg seperated the dollar and change amounts into two serpate HTML tags.
#Searching through the html tag labled strong and sup
strong = parent.find("strong") #This gets the first part of the price
sup = parent.find("sup") #This gets the change

#Prints information when you run the program
print(strong.string + sup.string)
