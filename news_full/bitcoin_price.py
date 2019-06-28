import requests, datetime
from bs4 import BeautifulSoup as bs

def bitcoin_price():
	search = requests.get("https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD")
	soup = bs(search.text, "html.parser")
	bitcoin_price = soup.find("span", class_ = "Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")
	try:
		bp = bitcoin_price.get_text().split()
		#t = datetime.datetime.now()
		#t = str(t.time())[:-7] + " -"
		#print(t, "$" + bp[0])
		print("\nBitcoin: $" + bp[0])
	except:
		pass
	

if __name__=='__main__':
	bitcoin_price()

#PS function  
# function bp {while(1){py .\bp2.py; start-sleep -seconds 180}}
