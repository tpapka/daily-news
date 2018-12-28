import requests
import subprocess
from bs4 import BeautifulSoup as bs

def get_news():
	top_stories = {}
	dd_list = []
	url = "https://news.ycombinator.com/"
	url2 = "https://www.drudgereport.com"

	r = requests.get(url)
	soup = bs(r.text, "html.parser")
	links = soup.findAll(class_="storylink")
	r = requests.get(url2)
	soup = bs(r.text, "html.parser")
	links2 = soup.findAll("a")
	for link in links2:
		try:
			if '...' in (link.string):
				dd_list.append(link)
		except:
			continue
			
	y_dd = [links, dd_list]
	print()
	i = 1
	
	for ydd in y_dd:
		if ydd == links:
			print(10*'-'+'TECH NEWS'+10*'-')
		else:
			print(10*'-'+'FRONT PAGE'+10*'-')
			
		for link in ydd:
			try:
				top_stories[str(i) + ". " + (link.string).upper()] = link['href']
				print(str(i) + ". " + ((link.string).replace('...','')).upper())
				i += 1
			except:
				continue
		print()

	print()
	pick = input("Type an article number or 'n' if you would like to close this program: ")

	while pick != 'n':
		for k,v in top_stories.items():
			if (pick + ". ").strip() == (k[:3]).strip():
				subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe', '-private-window', v])
		pick = input("Type an article number or 'n' if you would like to close this program: ")

if __name__ == '__main__':
	get_news()

	

#import itertools
#for a, b in itertools.zip_longest(list1, list2, fillvalue=''):
#	print('{:10}{:5}{}'.format(a, "|",b))

#def header():
	#print(100*"_")
	#print("{:50}{:50}{}".format("|", "|", "|"))
	#print("{:25}{:25}{:25}{:25}{:25}".format("|", "TECH NEWS", "|", "WORLD NEWS","|"))
	#print("|" + 49*"_" + "|" + 49*"_" + "|")
	
