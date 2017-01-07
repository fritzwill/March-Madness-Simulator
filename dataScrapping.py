# Web Scraper to get the names of teams in each round of the march madness tournament for a specific year
# Author: Will Fritz
# Date: 1/7/2017

# needed for web scrapping
import urllib2
from bs4 import BeautifulSoup

# the url we are using
url = "http://www.sports-reference.com/cbb/postseason/2010-ncaa.html"

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
# list containing all the above
grandList = [sAll, sRoundOne, sRoundTwo, sRoundThree, sRoundFour, sRoundFive, 
eAll, eRoundOne, eRoundTwo, eRoundThree, eRoundFour, eRoundFive,
mAll, mRoundOne, mRoundTwo, mRoundThree, mRoundFour, mRoundFive,
wAll, wRoundOne, wRoundTwo, wRoundThree, wRoundFour, wRoundFive]

################# POPULATING LISTS #################
regions = ['south', 'east', 'midwest', 'west']
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

print grandList[23]





