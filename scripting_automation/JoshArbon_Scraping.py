from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = 'https://neumont.smartcatalogiq.com/en/2024-2025/2024-2025/academic-calendar-2024-2025/'
page = urlopen(url)


soup = BeautifulSoup(page, 'html.parser')
calender = soup.find_all('table')

for table in calender:
    caption = table.find('caption')
    print("\n\n\n")
    print(caption.text)
    table_bodies = table.find_all('tbody')
    for body in table_bodies:
        table_data = []
        table_row = body.find_all('tr')
        for row in table_row:
            data = row.find_all('td')
            for t_data in data:
                table_data.append(t_data.text)
            table_data.append("\n")
        for thing in range(len(table_data)):
            table_data[thing] = table_data[thing].replace('\xa0', "").strip()

        for thing in range(int(len(table_data)/3)):
            table_data[thing] = table_data[thing].replace('\xa0', "")
            date_len = len(table_data[thing * 3])
            print(" " * (15 - date_len) + f"{table_data[thing * 3]}" + (" " * 4) + f" {table_data[thing * 3 + 1]}")
            print()