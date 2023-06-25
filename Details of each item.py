product_code_and_availability = soup.find_all('div', class_='description')
            for code in product_code_and_availability:
                product_data['product_code_and_availability'] = code.text

            price = soup.find_all('span', class_='price-new')
            for prices in price:
                product_data['price'] = prices.text

            description = soup.find_all('div', class_='tab-content')
            for descriptions in description:
                product_data['description'] = descriptions.text