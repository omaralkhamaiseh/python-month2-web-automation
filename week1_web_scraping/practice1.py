from bs4 import BeautifulSoup
with(open('practice1.html','r')) as f:
    read=BeautifulSoup(f,'html.parser')
storename=read.find('h1')
products=read.find_all('div',class_='product')
print(f"Store Name: {storename.get_text(strip=True)}")
for product in products:
    name=product.find('h2')
    price=product.find('p',class_='price')
    print(f"Product: {name.get_text(strip=True)}")
    print(f"Price: {price.get_text(strip=True)}")