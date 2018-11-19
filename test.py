import requests
from bs4 import BeautifulSoup

baseURL = "https://www.thinkgeek.com/accessories/"
categories = {'jewelry/': 'Jewelry', 'footwear/': 'Footwear', 'keychains/': 'Keychains & Bag Accessories',
              'wallets/': 'Wallets', 'hats-hair/': 'Hats & Hair', 'ties-cufflinks/': 'Ties & Cufflinks',
              'belts-suspenders/': 'Belts & Suspenders', 'scarves/': 'Scarves', 'cosmetics-body/': 'Cosmetics & Body',
              'purses-handbags/': 'Purses & Handbags', 'pouches-coin-purses/': 'Pouches & Coin Purses',
              'other/': 'Other Accessories'}

for c in categories:
    cat = categories[c]
    print(cat)

