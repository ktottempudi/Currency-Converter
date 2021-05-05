from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import urllib.parse
import urllib.request
import re
from bs4 import BeautifulSoup

class serverHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Content_type', 'text/html')
		self.end_headers()

		rate = ""

		upPath = parse_qs(self.path[2:]) # Parse incoming url for parameters

		if upPath != {}:
			rate = findRate(str(upPath['fcurrency']), str(upPath['scurrency']))

		output = bytes(str(rate), "UTF-8")
		self.wfile.write(output)


def findRate(fcurrency, scurrency):
	first = ''.join(c for c in fcurrency if c not in "'[']") # Removes specified elements
	second = ''.join(c for c in scurrency if c not in "'[']")
	url = "https://www.google.com/search?q=convert+{}+to+{}".format(first, second)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel OS X 10_9_3) AppleWebKit/537.36 (HTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
	request = urllib.request.Request(url, headers=headers)
	response = urllib.request.urlopen(request)
	page = response.read().decode('UTF-8')
	soup = BeautifulSoup(page, "html.parser")
	parse_data = soup.find_all("div", class_="BNeawe iBp4i AP7Wnd")[-1]
	rate = re.sub('[^0-9.]', '', parse_data.get_text()) # Remove anything not a digit from expression

	return rate
