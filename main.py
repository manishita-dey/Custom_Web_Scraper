from bs4 import BeautifulSoup
import requests
import pandas


# Creating response request for the website
endpoint = 'https://www.alibaba.com/products/paracord.html?IndexArea=product_en'
response = requests.get(endpoint)
website = response.text


# Creating soup from the response received
soup = BeautifulSoup(website, 'html.parser')


total_pages = 100


item_name_list = []
item_price_list = []
item_volume_list = []



for page in range(100):
    response = requests.get(f'{endpoint}&pages={page+1}')
    website = response.text
    soup = BeautifulSoup(website, 'html.parser')

    # Scraping Product name
    all_item_name = soup.find_all(name = 'p', class_ = 'elements-title-normal__content')
    for name in all_item_name:
        item_name_list.append(name.getText())

    #Scraping Product Price
    all_item_price = soup.find_all(name = 'span', class_ = 'elements-offer-price-normal__price')
    for price in all_item_price:
        item_price_list.append(price.getText())

    # Scraping min volume of Product that can be ordered
    all_item_volume = soup.find_all(name='p', class_='element-offer-minorder-normal')
    for volume in all_item_volume:
        item_volume_list.append(volume.getText())


records = {"Item Name": item_name_list ,
           "Item Price":item_price_list,
           "Item Min Volume":item_volume_list,
           }

# Creating csv file
pandas.DataFrame(records).to_csv("Alibaba Product Details.csv", index=True)



