import urllib
import re
from bs4 import BeautifulSoup
import csv

L =dict()
k = []
web_to_search = raw_input('Enter--\n')
html = urllib.urlopen(web_to_search).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('a')
for tag in tags:
	try:
		content = tag.contents[0].encode('utf-8')
		x = re.findall('\S+@\S+',content)
		y = re.findall('^Dr.*',content)
		if len(x) > 0:
			email = x[0]
		if len(y) > 0:
			name = y[0]
		else:
			name = "not found"
			#L[name] = email
		links = tag.get('href', None)
		#print links
		profile_link = re.findall('\S+people-profiles\S+',links)
		if len(profile_link) > 0:
			open_profile =urllib.urlopen(profile_link[0]).read()
			second_soup = BeautifulSoup(open_profile,'html.parser')
			pre_research = second_soup.find('div',{"class":"field field-name-body field-type-text-with-summary field-label-hidden"})
			research = pre_research.find('div', {"class":"field-item even"})
			a =research.find('ul')
			b = a.get_text()
			sentences = b.split('\n')
			sentences.insert(0,email)
			L[name] = sentences
			## split text into list
			
	except:
		pass
		# try:
			# content = tag.contents[0].encode('utf-8')
			# x = re.findall('\S+@\S+',content)
			# y = re.findall('^Dr.*',content)
			# if len(x) > 0:
				# email = x[0]
			# if len(y) > 0:
				# name = y[0]
			# else:
				# name = "not found"
			# L[name] = email
			
		# except:
			# pass
print L

with open('profile.csv', 'wb') as f:
    writer = csv.writer(f)
    for row in L.iteritems():
        writer.writerow(row)	