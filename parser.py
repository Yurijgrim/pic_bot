import requests,pyshorteners
from bs4 import BeautifulSoup
	 
 
def get(url,pattern="/"):
	arr =[]
	r = requests.get(url)
	soup_ing = str(BeautifulSoup(r.content, 'html'))

	def fromSoup(data):
		html_file = data
		soup = BeautifulSoup(html_file, 'html') # name of our soup
		for link in soup.find_all('a'):
			dt = str(link.get('href'))
			if dt.find("view") != -1:
				if dt.find("files") == -1:
					if link.get('href') not in arr:
						arr.append(link.get('href'))
			# print(link.get('href'))    
		return arr
	return fromSoup(soup_ing)

def startpages(url, mode, range_a, range_b):
	arr =[]
	for i in range(range_a,range_b):
		u = url+"p"+str(i)
		print(u)
		if u not in arr:
			arr.append(get(u, mode))
	return arr
