import urllib2
from bs4 import BeautifulSoup

# the url we are using
url = "http://www.sports-reference.com/cbb/seasons/2010-school-stats.html"

# query website and return the html
page = urllib2.urlopen(url)

soup = BeautifulSoup(page, "html.parser")

data = soup.find('table', class_='sortable stats_table')
print data