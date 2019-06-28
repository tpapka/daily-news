import requests
from bs4 import BeautifulSoup as bs

def market_indexes():
	search = requests.get("https://finance.yahoo.com/")
	soup = bs(search.text, "html.parser")
	sp = soup.find("span", {"data-reactid":7})
	sp_change = soup.find("span", {"data-reactid":8})
	dow = soup.find("span", {"data-reactid":12})
	dow_change = soup.find("span", {"data-reactid":13})
	nas = soup.find("span", {"data-reactid":17})
	nas_change = soup.find("span", {"data-reactid":18})
	# sp_test = soup.find("li", {"aria-label":"Nasdaq"})
	# print(sp_test)
	try:
		print("DOW 30: " + dow.get_text() + " " + dow_change.get_text())
		print("S&P 500: " + sp.get_text() + " " + sp_change.get_text())
		print("Nasdaq: " + nas.get_text() + " " + nas_change.get_text())
	except:
		pass
	

if __name__=='__main__':
	market_indexes()

#PS function  
# function bp {while(1){py .\bp2.py; start-sleep -seconds 180}}
