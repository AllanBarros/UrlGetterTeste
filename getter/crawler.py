import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup

total_urls_visited = 0

def is_valid(url):
 
    # Check para url valida
    
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url, urls_list):
    # Retorna todas as URL's localizadas na URL inicial
    
    urls = set()

    #Usa o BeautifulSoup para pegar a página HTML como um todo 
    # e assim localizar os links definidos como href no html
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # em caso de estar vazio tag vazia
            continue
        # join na URL em caso do link não ser absoluto
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove parametros e outras coisas da URL
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # caso não seja valida a URL
            continue
        if href not in urls_list:
            #adiciona se for uma nova url
            urls_list.add(href)
        urls.add(href)
    return urls


def crawl(url, max_urls, urls_list):

    #Faz a verificação da quantidade de urls visitadas
    # (limitada para caso de problemas de performance ou bloqueio)
    # chama função recursivamente até o total de urls visitadas
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url, urls_list)
    for link in links:
        if total_urls_visited > max_urls:
            return urls_list
        crawl(link, max_urls, urls_list)