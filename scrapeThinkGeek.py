import requests
from bs4 import BeautifulSoup

baseURL = "https://www.thinkgeek.com/"
categories = {'clothing/': 'Clothing', 'accessories/': 'Accessories', 'bags-backpacks/': 'Bags & Backpacks',
              'home-office/': 'Home & Office', 'toys-games/': 'Toys &  Games', 'collectibles/': 'Collectibles',
              'tools-outdoor-survival/': 'Tools, Outdoor & Survival', 'electronics-gadgets/': 'Electronics & Gadgets'}
for c in categories:
    cat = categories[c]
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
                if onSale == 1:
                    sale = "Yes"
                else:
                    sale = "No"
                savings = product.get('data-sale-percent-savings')
                fandom = product.get('data-fandom').replace('["', '').replace('"]', '')
                character = product.get('data-character').replace('["', '').replace('"]', '')
                stock = product.find_all('p', attrs={'class': 'outofstock'})
                if len(stock) > 0:
                    inStock = "Out of Stock"
                else:
                    inStock = "In Stock"
                print(name, price, sale, savings, cat, fandom, character, inStock)
            counter += 1
        else:
            print("No more items!")
            break

print("Scraping complete")