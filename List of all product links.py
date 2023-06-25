product_link = []
        link = soup.find_all('div',class_='name')
        for links in link:
            i = links.find_all('a')
            for d in i:
                result = d.get('href')
                if result not in product_link:
                    product_link.append(result)