import requests
from bs4 import BeautifulSoup


def pars():
    url = 'https://auto.drom.ru/toyota/mark_ii/generation7/restyling0/'
    params = {'page': 1}
    pages = 2
    n = 1

    while params['page'] <= pages:
        response = requests.get(url, params=params)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('a', class_='css-ck6dgx ewrty961')

        for n, i in enumerate(items, start=1):
            itemName = i.find('div', class_='css-13ocj84 e727yh30').text.strip()
            itemPrice = i.find('span', class_='css-46itwz e162wx9x0').text
            print(f'{n}:  {itemName} | за {itemPrice}')

        last_page_num = int(soup.find_all('a', class_='css-1jjais5 ena3a8q0')[-2].text)
        pages = last_page_num if pages < last_page_num else pages
        params['page'] += 1


if __name__ == '__main__':
    pars()
