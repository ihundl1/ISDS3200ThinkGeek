import csv
import requests
import datetime
from bs4 import BeautifulSoup

now = datetime.datetime.now()

csvFile = open('thinkGeekProducts.csv', 'a', newline='')
writer = csv.writer(csvFile)
#writer.writerow(['Date', 'Product Name', 'Category', 'Subcategory', 'Price', 'Sale', 'Savings', 'Fandom', 'Character',
#                 'Stock'])

baseURL = "https://www.thinkgeek.com/accessories/"
categories = {'jewelry/': 'Jewelry', 'footwear/': 'Footwear', 'keychains/': 'Keychains & Bag Accessories',
              'wallets/': 'Wallets', 'hats-hair/': 'Hats & Hair', 'ties-cufflinks/': 'Ties & Cufflinks',
              'belts-suspenders/': 'Belts & Suspenders', 'scarves/': 'Scarves', 'cosmetics-body/': 'Cosmetics & Body',
              'purses-handbags/': 'Purses & Handbags', 'pouches-coin-purses/': 'Pouches & Coin Purses',
              'other/': 'Other Accessories'}
for c in categories:
    cat = categories[c]

    print("Scraping ", cat)
    counter = 0
    while True:
        pageLoop = "feature/desc/" + str(counter) + "/100/"
        url = baseURL + c + pageLoop

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        products = soup.find_all('div', attrs={'class': 'product'})
        if len(products) > 0:
            for product in products:
                name = product.get('data-name')
                p = product.get('data-price').replace('$', '')
                try:
                    price = float(p)
                except ValueError:
                    price = 0
                onSale = product.get('data-on-sale')
                if onSale == "1":
                    sale = "TRUE"
                else:
                    sale = "FALSE"
                savings = product.get('data-sale-percent-savings')
                fandom = product.get('data-fandom').replace('["', '').replace('"]', '')
                character = product.get('data-character').replace('["', '').replace('"]', '')
                stock = product.find_all('p', attrs={'class': 'outofstock'})
                if len(stock) > 0:
                    inStock = "Out of Stock"
                else:
                    inStock = "In Stock"
                writer.writerow([now.date(), name, 'Accessories', cat, price, sale, savings, fandom,
                                 character.encode("utf-8"), inStock])
            counter += 1
        else:
            print("End of ", cat)
            break

print("Scraping complete")