def parse_bs4(parse_function, html_source_list, result):
    for html in html_source_list:
        result.append(parse_function(html))
