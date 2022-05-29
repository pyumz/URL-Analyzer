from urllib import request
from urllib.parse import urlparse
from lxml import html
import requests

def get_urls_from_string(page_content, base_url):
    content = html.fromstring(page_content)
    content.make_links_absolute(base_url=base_url)

    url_list = []
    for elem in content.iter():
        if elem.tag == "a":
            url_list.append(elem.get("href"))
    return url_list

def normalize_url(url):
    normal_url = urlparse(url)

    parsed_url = "{}{}".format(normal_url.netloc, normal_url.path)
    lowercase_url = parsed_url.lower()

    slash_removed = lowercase_url if lowercase_url[-1] != "/" else lowercase_url[:-1]

    return slash_removed

def crawl_pages(base_url, current_url, pages):

    normalized_url = normalize_url(base_url)

    if normalized_url not in pages:
        pages[normalized_url] = 0

    if urlparse(base_url).netloc != urlparse(current_url).netloc:
        pages[normalized_url] = None
        return pages

    if pages[normalized_url] == None:
        return pages

    if pages[normalized_url] > 0:
        pages[normalized_url] += 1
        return pages

    req = requests.get(current_url)

    try:
        validate_response(req, base_url)
    except Exception as e:
        print(e)
        pages[normalized_url] = None
        return pages
    
    pages[normalized_url] += 1

    urls = get_urls_from_string(req.content, base_url)

    for url in urls:
        pages[url] = 1
        
    return pages

def validate_response(resp, url):
    if resp.status_code != 200:
        raise Exception("The URL provided, {}, did not return a successful status code but instead returned {}".format(url, resp.status_code))
    
    if "text/html" not in resp.headers['content-type'].lower():
        raise Exception("{} does not contain correct headers but instead returned {}".format(url, resp.headers['content-type']))

