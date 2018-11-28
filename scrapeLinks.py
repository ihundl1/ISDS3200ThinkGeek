import requests
import csv
from bs4 import BeautifulSoup

csvFile = open('productLinks.csv', 'w', newline='')
writer = csv.writer(csvFile)
writer.writerow(['Name', 'Link'])

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
                tag = product.find('a')
                link = tag.get('href')
                writer.writerow([name, link])
            counter += 1
        else:
            print("End of ", cat)
            break

print("Scraping complete")
