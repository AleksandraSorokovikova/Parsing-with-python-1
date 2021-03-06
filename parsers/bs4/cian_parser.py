from bs4 import BeautifulSoup

def parse_cian_bs4(html_source):
    response = BeautifulSoup(html_source, 'html.parser')
    cards = response.select(r'[data-name="CardComponent"]')
    
    products = []
    
    for card in cards:
        name = card.select_one(r'[data-name="TitleComponent"]').text.strip()
        price = card.select_one(r'[data-mark="MainPrice"]').text.strip()
        location = ','.join([x.text.strip() for x in card.select(r'[data-name="GeoLabel"]')])
        yield { 'name': name,
               'price': price,
               'location': location }
