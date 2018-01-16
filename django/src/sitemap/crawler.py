import re
import requests
import logging
logger = logging.getLogger('default')
from urllib.parse import urlsplit, urlunsplit, urljoin, urlparse

class Crawler:
    def __init__(self, url):
        logger.info('__init__')
        self.url = self.normalize(url)
        self.host = urlparse(self.url).netloc
        self.found_links = []
        self.visited_links = [self.url]

    def start(self):
        logger.info('start')
        self.crawl(self.url)
        return self.found_links

    def crawl(self, url):
        logger.info('crawl')
        response = requests.get(url, verify=False)
        page = response.text
        pattern = '<a [^>]*href=[\'|"](.*?)[\'"].*?>'
        found_links = re.findall(pattern, page)
        links = ['/ru/',]
        for link in found_links:
            logger.info('FOUNDLINK: '+link)
            is_url = self.is_url(link)
            if is_url:
                is_internal = self.is_internal(link)
                if is_internal:
                    self.add_url(link, links)
                    self.add_url(link, self.found_links)
        for link in links:
            logger.info('LINK: '+link)
            if link not in self.visited_links:
                link = self.normalize(link)
                self.visited_links.append(link)
                self.crawl(urljoin(self.url, link))

    def add_url(self, link, link_list):
        link = self.normalize(link)
        if link:
            not_in_list = link not in link_list and link.replace('/', '') not in link_list
            excluded = False
            if not_in_list and not excluded:
                link_list.append(link)

    def normalize(self, url):
        scheme, netloc, path, qs, anchor = urlsplit(url)
        return urlunsplit((scheme, netloc, path, qs, anchor))

    def is_internal(self, url):
        host = urlparse(url).netloc
        return host == self.host or host == ''

    def is_url(self, url):
        scheme, netloc, path, qs, anchor = urlsplit(url)
        if url != '' and scheme in ['http', 'https', '']:
            return True
        else:
            return False
