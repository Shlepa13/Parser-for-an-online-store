import requests
from bs4 import BeautifulSoup
import json

data = []

# online store - https://www.everbrightinc.com/
for category in ['67_68','67_74','67_73','67_72','67_70','67_69','67_71', # - WOMEN
                 '75_79','75_77','75_78','75_76',                         # - MEN
                 '84_85','84_86',                                         # - GIRL
                 '80_81','80_83','80_82',                                 # - BOY
                 '91_92',                                                 # - BABY not available
                 '93',                                                    # - SALES
                 '95',                                                    # - HOLIDAYS
                 '103']:                                                  # - NEW
    for page in range(1, 8):
        url = f'https://www.everbrightinc.com/index.php?route=product/category&path={category}&page={page}'


        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')

        product_link = []
        link = soup.find_all('div',class_='name')
        for links in link:
            i = links.find_all('a')
            for d in i:
                result = d.get('href')
                if result not in product_link:
                    product_link.append(result)

        for link in product_link:
            product_page = requests.get(link)
            soup = BeautifulSoup(product_page.text, 'lxml')
            product_data = {}

            product_code_and_availability = soup.find_all('div', class_='description')
            for code in product_code_and_availability:
                product_data['product_code_and_availability'] = code.text

            price = soup.find_all('span', class_='price-new')
            for prices in price:
                product_data['price'] = prices.text

            description = soup.find_all('div', class_='tab-content')
            for descriptions in description:
                product_data['description'] = descriptions.text

            data.append(product_data)
            with open('goods.json','w') as f:
                json.dump(data,f,ensure_ascii=False,indent=4)
