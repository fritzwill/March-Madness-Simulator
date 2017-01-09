# Web Scraper to get the names of teams in each round of the mens NCAA march madness tournament for a specific year
# The scraper works for sports-reference.com, specifically the "NCAA tournament" for a specific year
# Sample url on which the web scraper works: http://www.sports-reference.com/cbb/postseason/2012-ncaa.html
# Use this scraper on sports-reference pages similar to the above url

# Author: Will Fritz
# Date: 1/7/2017

# needed for web scrapping
import urllib2
from bs4 import BeautifulSoup
# needed for creating csv file
import csv

# the following must be changed relative to each year
url = "http://www.sports-reference.com/cbb/postseason/2016-ncaa.html" # url of page being scraped
outputName = "season2016.csv" # use template example (change year as needed): season2010.csv 
regions = ['east', 'west', 'south', 'midwest'] # must be changed relative to each year (look at what webpage has for each region)

# query website and return the html
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

###################### LISTS ######################
# each respective round in the South 
sAll = [] # every team
sRoundOne = []
sRoundTwo = []
sRoundThree = []
sRoundFour = []
sRoundFive = []
# each respective round in the East 
eAll = [] # every team
eRoundOne = []
eRoundTwo = []
eRoundThree = []
eRoundFour = []
eRoundFive = []
# each respective round in the Midwest
mAll = [] # every team
mRoundOne = []
mRoundTwo = []
mRoundThree = []
mRoundFour = []
mRoundFive = []
# each respective round in the West
wAll = [] # every team
wRoundOne = []
wRoundTwo = []
wRoundThree = []
wRoundFour = []
wRoundFive = []
# each round starting with final 4
finalFour = []
championship = []
champion = []
# list containing all the above
grandList = [sAll, sRoundOne, sRoundTwo, sRoundThree, sRoundFour, sRoundFive, 
eAll, eRoundOne, eRoundTwo, eRoundThree, eRoundFour, eRoundFive,
mAll, mRoundOne, mRoundTwo, mRoundThree, mRoundFour, mRoundFive,
wAll, wRoundOne, wRoundTwo, wRoundThree, wRoundFour, wRoundFive,
finalFour, championship, champion]

################# POPULATING LISTS #################
grandListCounter = 0 # used to access each list in grandList
for r in regions: 
	region = soup.find('div', {'id':r})
	regionAll = region.find_all('a')
	
	# pupulates sAll, eAll, mAll, wAll
	# takes the 1st and 3rd link text out of groupings of five
	ignoreCount = 0 # used to determine what link text to obtain
	for a in regionAll:
		if ignoreCount == 4:
			ignoreCount = -1 
		if ignoreCount%2 == 0:
			grandList[grandListCounter].append(a.string)
		ignoreCount += 1
	
	# populate an array for each round
	roundCount = 0
	for team in grandList[grandListCounter]:
		if roundCount == 30:
			grandListCounter += 1
			grandList[grandListCounter].append(team)
		elif roundCount <= 29 and roundCount > 27:
			if roundCount == 28:
				grandListCounter += 1
			grandList[grandListCounter].append(team)
		elif roundCount <= 27 and roundCount > 23:
			if roundCount == 24:
				grandListCounter += 1
			grandList[grandListCounter].append(team)
		elif roundCount <= 23 and roundCount > 15:
			if roundCount == 16:
				grandListCounter += 1
			grandList[grandListCounter].append(team)
		else:
			if roundCount == 0:
				grandListCounter += 1
			grandList[grandListCounter].append(team)
		roundCount += 1

	grandListCounter += 1

# national: composed of final four teams
national = soup.find('div', {'class':'team4'})
nAll = national.find_all('a')

ignoreCount = 0
for n in nAll:
		if ignoreCount == 16:
			grandListCounter += 1
			ignoreCount = 17
		if ignoreCount == 10:
			grandListCounter += 1
			ignoreCount = 11
		if ignoreCount == 4:
			ignoreCount = 5
		if ignoreCount%2 == 0:
			grandList[grandListCounter].append(n.string)
		ignoreCount += 1

#################### OUTPUT CSV ####################
counterRange1 = range(1, 6)
counterRange2 = range(7, 12)
counterRange3 = range(13, 18)
counterRange4 = range(19, 24)
counterRange5 = range(24,27)

with open(outputName,'wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in counterRange1:
		filewriter.writerow(grandList[i])
	for i in counterRange2:
		filewriter.writerow(grandList[i])
	for i in counterRange3:
		filewriter.writerow(grandList[i])
	for i in counterRange4:
		filewriter.writerow(grandList[i])
	for i in counterRange5:
		filewriter.writerow(grandList[i])




