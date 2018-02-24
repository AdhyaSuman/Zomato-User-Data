import re
from bs4 import BeautifulSoup
import requests

def extract_link(url):
	"""
	Creates a BeautifulSoup object from the link
	:param url: the link
	:return: a BeautifulSoup object equivalent of the url
	"""
	headers = {"Host": "www.zomato.com",
	       "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0",
	       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	       "Accept-Language": "en-US,en;q=0.5",
	       "Accept-Encoding": "gzip, deflate, br",
	       "Referer": "https://www.zomato.com/",
	       "Connection": "keep-alive"}
	while(1):
		try:
			r = requests.get(url, headers=headers)
		except requests.exceptions.Timeout:
			continue
		break
	if r.status_code == 404:
		return None
	doc = r.content
	soup = BeautifulSoup(doc,'html.parser')
	with open ('zomata_user_data', "a") as filew:
		filew.write('\n\n##\n\n')
		ptags = soup.find_all('title')
		str = ptags[0].string
		re.sub('<title>','',str)
		re.sub('</title>','',str)
		str = str.strip()
		str = str[:-9]
		lst = str.split(',')
		filew.write(lst[0].strip()+'\n')
		if(len(lst)>1):
			filew.write(lst[1].strip()+'\n')

		ptags = soup.find_all("a", 'item user-tab user-tab-reviews cursor-pointer ')
		lis = ptags[0].find_all('div')
		str = lis[0].string
		re.sub('<div class="ui label">','',str)
		re.sub('</div>','',str)
		filew.write('Reviews = '+str+'\n')

		ptags = soup.find_all("a", 'item user-tab user-tab-blogs cursor-pointer ')
		if(ptags):
	
			lis = ptags[0].find_all('div')	
			str = lis[0].string
			re.sub('<div class="ui label">','',str)
			re.sub('</div>','',str)
			filew.write('Blog posts = '+str+'\n')

	

		ptags = soup.find_all("a", 'item user-tab-follows user-tab cursor-pointer ')
		lis = ptags[0].find_all('div')
		str = lis[0].string
		re.sub('<div class="ui label">','',str)
		re.sub('</div>','',str)
		filew.write('Followers = '+str+'\n')

		ptags = soup.find_all("a", 'item user-tab user-tab-bookmarks cursor-pointer ')
		lis = ptags[0].find_all('div')
		str = lis[0].string
		re.sub('<div class="ui label">','',str)
		re.sub('</div>','',str)
		re.sub(' | Zomato','',str)
		filew.write('Bookmarks = '+str+'\n')
	
		#item user-tab user-tab-beenthere cursor-pointer 
		ptags = soup.find_all("a", 'item user-tab user-tab-beenthere cursor-pointer ')
		lis = ptags[0].find_all('div')
		str = lis[0].string
		re.sub('<div class="ui label">','',str)
		re.sub('</div>','',str)
		filew.write('Been there = '+str+'\n')
	
		ptags = soup.find_all("div", 'user-stats_ranking')
		lis = ptags[0].find_all('span',{'data-icon' : 'ú'})
		str = lis[0].string
		#print(str)
		filew.write('Foodie level = '+str+'\n')
		
		if(str != '13'):
			ptags = soup.find_all("section", 'user-cover ptop ta-center')
			lis = ptags[0].find_all('div','ui mini statistics')
			lcs = lis[0].find_all('div', {'class':"label"})
			str = lcs[0].string
			#print(str)
			str = str.strip()
			filew.write(str+'\n')
		else:
			filew.write('0 points to level up\n')

		linkset = set()
		row = soup.find('div', 'row tac user-cover')
		lst = row.find('a',{'class':"floating ui blue circular label tooltip_formatted verified-profile"})
		if(lst):
		#	print (lst)
			filew.write("Verified User\n")
		else:
			filew.write('Not a verified user\n')


		utag = soup.find('div','ui popup user-common-section user-expertise expertise_popup hidden')
		if(utag):
			ptags = utag.find_all("li", 'badge')
			neighbour = set()
			for i in range(0,len(ptags)):
				str = ptags[i].get_text()
				p = ''
				for j in range(0,len(str)):
					if str[j] == ' ' and j+1<len(str) and str[j+1] == ' ':
						continue
					p = p + str[j]
	
				p = p.strip()
				#print(p)
				neighbour.add(p)
			total = repr(len(neighbour)) + ' Neighbourhoods'
			filew.write(total+'\n')
			for i in neighbour:
				filew.write(i+'\n')
		
		else:
			filew.write('0 Neighbourhoods\n')


def extract_user_data():
	with open ('skip_lines', "r") as myfile:
		skip = int(myfile.readline()) 
	with open ('user-links', "r") as myfile:
		for skiplines in range(skip):
			skiptext = myfile.readline()
		for line in myfile.readlines():
			line = line.strip()
			#print(line)
			skip = skip + 1
			extract_link(line)
			#with open ('user_links', "a") as myfile2:
			#	for item in userset:
			#		myfile2.write(item+'\n')
			with open ('skip_lines', "w") as myfile1:
				myfile1.write(str(skip))

extract_user_data()

