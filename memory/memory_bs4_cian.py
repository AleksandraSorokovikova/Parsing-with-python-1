
from parsers.bs4.cian_parser import parse_cian_bs4
from parsers.bs4.parse_bs4 import parse_bs4

html_source_list_bs4 = ['/Users/alexandrasorokovikova/2 курс/new project/Parsing-with-python-1/tests/cian/test_source/test{0}.html'.format(i) for i in range(1, 51)]
html_source_list_scrapy = ['file:/Users/alexandrasorokovikova/2 курс/new project/Parsing-with-python-1/tests/cian/test_source/test{0}.html'.format(i) for i in range(1, 51)]

html_files = []
for html in html_source_list_bs4:
    with open(html) as html_file:
        html_files.append(html_file.read())
        
def select_pages(page_limit, pages):
    return pages[:page_limit]

@profile
def test_bs4():
    for page_limit in range(1, 51):
        pages = select_pages(page_limit, html_files)
        habr_data = []

        parse_bs4(parse_cian_bs4, pages, habr_data)
        
test_bs4()
