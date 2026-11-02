from bs4 import BeautifulSoup
with(open('practice2.html','r')) as f:
    read=BeautifulSoup(f,'html.parser')
products=read.find_all('div',class_='product') 
for product in products:
    name=product.find('h2')
    price=product.find('p',class_='price')
    print(f"Product: {name.get_text(strip=True)}")
    if price ==None:
        print("Price: Not available")
    else:
        print(f"Price: {price.get_text(strip=True)}")