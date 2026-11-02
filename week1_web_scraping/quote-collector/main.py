from bs4 import BeautifulSoup
import requests
url='https://quotes.toscrape.com/?utm_source=chatgpt.com'
def fetch_quotes(url):
    results=[]
    response=requests.get(url,timeout=10)
    response.raise_for_status()  # Raise an error for bad responses
    html=response.text
    read=BeautifulSoup(html,'html.parser')
    quotes=read.find_all('div',class_='quote')
    for quote in quotes[0:10]:
        text=quote.find('span',class_='text')
        author=quote.find('small',class_='author')
        quote_data={
            "Quote":text.get_text(strip=True),
            "Author":author.get_text(strip=True)
        }
        results.append(quote_data)
    return results
def save_quotes(data):
    with open('quotes.txt', 'w', encoding='utf-8') as f:
        for quote in data:
            f.write(f"Quote: {quote['Quote']}\n")
            f.write(f"Author: {quote['Author']}\n\n")
data = fetch_quotes(url)
save_quotes(data)            