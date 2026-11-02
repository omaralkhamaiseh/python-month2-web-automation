from bs4 import BeautifulSoup
import requests
url='https://quotes.toscrape.com/?utm_source=chatgpt.com'
response=requests.get(url,timeout=10)
response.raise_for_status()  # Raise an error for bad responses
html=response.text
read=BeautifulSoup(html,'html.parser')
quotes=read.find_all('div',class_='quote')
for quote in quotes[0:5]:  # Limit to first 5 quotes
    text=quote.find('span',class_='text')
    author=quote.find('small',class_='author')
    print(f"Quote:{text.get_text(strip=True)}")
    print(f"Author:{author.get_text(strip=True)}")
