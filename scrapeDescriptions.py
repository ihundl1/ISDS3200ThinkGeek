import requests
import csv
from bs4 import BeautifulSoup

csvFile = open('productLinks.csv', 'r')
next(csvFile)
read = csv.reader(csvFile)

newFile = open('productDescriptions.csv', 'w', newline='')
writer = csv.writer(newFile)
writer.writerow(['Name', 'Description'])

baseURL = "https://www.thinkgeek.com"

for row in read:
    name = row[0]
    ext = row[1]

    url = baseURL + ext
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    desc = soup.find('div', attrs={'id': 'proddescription'}).text.strip()

    print(name)
    writer.writerow([name, desc])


print("Scraping Complete!")
