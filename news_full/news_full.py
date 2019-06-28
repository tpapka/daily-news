import requests
import subprocess
from market_indexes import market_indexes as mi
from bp3 import bitcoin_price as price
from bs4 import BeautifulSoup as bs

def get_news():
	top_stories = {}
	url = "https://news.ycombinator.com/"

	r = requests.get(url)
	soup = bs(r.text, "html.parser")
	links = soup.findAll(class_="storylink")
	print()

	for i, link in enumerate(links):
		top_stories[str(i + 1) + ". " + (link.string).title()] = link['href']
		print(str(i + 1) + ". " + (link.string).title())

	print()
	pick = input("Type an article number or 'n' if you would like to close this program: ")

	while pick != 'n':
		for k,v in top_stories.items():
			if (pick + ". ").strip() == (k[:3]).strip():
				subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe', '-private-window', v])
		pick = input("Type an article number or 'n' if you would like to close this program: ")

if __name__ == '__main__':
	price()
	mi()
	get_news()
