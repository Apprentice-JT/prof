import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import csv

L =dict()
k = []
n = []
email_list = []
count = 0
email_count = 0	
web_to_search = raw_input('Enter--\n')
html = urllib.urlopen(web_to_search).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('a')
for tag in tags:
	
	
	try:
		links = tag.get('href', None)
		y = re.findall('\S+people/\S+',links)
		if len(y) > 0 :
			y[0]="http:"+y[0]
			if (y[0] not in k) :
				
				k.append(y[0])
		
			name = tag.contents[0].encode('utf-8')
			a = re.sub('<[^<]+?>', '', name)
			if (len(a)>0):
				n.append(a)
			
	except:
		pass
		# k.append(y[0])
		# name = tag.contents[0].encode('ascii', 'ignore')
		# n.append(name)

k = k[5:]
n = n[5:]
print k
print n
for link in k:
	Prof_name = n[count]
	open_profile =urllib2.urlopen(link,timeout = 10000).read()
	second_soup = BeautifulSoup(open_profile,'html.parser')
	second_tags  =  second_soup("span")
	
	for second_tag in second_tags:
		try:
			name_text_tag = second_tag.find_all('span',{'class':'u'})
			if len(name_text_tag) >0:
				email = name_text_tag[0].get_text().replace(' [dot] ',".")+'@mcgill.ca'
				email_list.append(email)
			
		except:
			pass

	# emails = second_soup(text = "E-mail")
	# for tag in second_soup.findAll(lambda tag: (tag.name == 'a' and tag.text == 'E-mail' and tag.attrs == {'class':'spamspan'}),href=True):
		# print tag['href']
	try:
		first_step = second_soup.find(text = re.compile("General information",re.IGNORECASE))
		text = first_step.findNext('p').contents[0].encode('ascii','ignore')
	except:
		text = "item cannot be found ",Prof_name
	if (Prof_name != 'Ronald Gehr'):
		L[Prof_name+" "+email_list[email_count]] = text
		count = count+1
		email_count = email_count+1
	else:
		L[Prof_name+" "+"No email"] = text
		count = count + 1



# with open('profile_mg2.csv', 'wb') as f:
    # writer = csv.writer(f)
    # for row in L.iteritems():
        # writer.writerow(row)