import urllib
import re
from bs4 import BeautifulSoup
import csv

L =dict()
k = []
n = []
email_list = []
count = 0	
web_to_search = raw_input('Enter--\n')
html = urllib.urlopen(web_to_search).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('a')
for tag in tags:
	links = tag.get('href', None)
	y = re.findall('\S+professors/\S+',links)
	if len(y) > 0:
		k.append(y[0])
		name = tag.contents[0].encode('ascii', 'ignore')
		n.append(name)
pos = len(k)/2
half_k = k[:pos]
half_n = n[:pos]
#print n
#print k
emails = soup.find_all('td',{"class":"column-5"})
for email in emails:
	content = email.contents[-1].encode('utf-8')
	a = re.sub('<[^<]+?>', '', content)
	email_list.append(a)
	
for link in half_k:
	Prof_name = half_n[count]
	Prof_email = email_list[count].replace("\n","")
	Prof_infor = Prof_name + " " + Prof_email
	print Prof_infor
	
	open_profile =urllib.urlopen(link).read()
	second_soup = BeautifulSoup(open_profile,'html.parser')
	try:
		first_step = second_soup.find(text = "Research Interests")
		text = first_step.findNext('p').contents[0].encode('ascii','ignore')
	except:
		text = "item cannot be found ", Prof_name
	print text
	L[Prof_infor] = text
	count = count + 1

print L

# with open('profile_ut.csv', 'wb') as f:
    # writer = csv.writer(f)
    # for row in L.iteritems():
        # writer.writerow(row)