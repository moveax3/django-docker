from .crawler import Crawler
import logging
logger = logging.getLogger('default')

def generate(domain, path):
    logger.info('start')
    url = 'https://' + domain
    logger.info('create sitemap for '+url)
    crawler = Crawler(url)
    logger.info('crawler start')
    links = crawler.start()
    logger.info('crawler end')
    for link in links:
        logger.info(link)
    with open(path, "w") as file:
        logger.info('writing to file')
        file.write(
            '<?xml version="1.0" encoding="UTF-8"?>\n\t<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

        excluded_links = [
            "#mobilemenu",
            '/ru/',
            '/',
            '#vk',
            '#fb',
            '#tw',
            '#ok',
            '#gg',
            '#error',
            '#close',
        ]
        for link in links:
            if link in excluded_links:
                continue
            fulllink = url+'/'+link
            fulllink = fulllink.replace('//ru', '/ru')
            if fulllink.count('https://') > 1:
                continue
            entrypoint = """
            <url>
                <loc>{0}/</loc>
                <changefreq>monthly</changefreq>
                <priority>0.8</priority>
            </url>""".format(fulllink)
            file.write(entrypoint)
        file.write('</urlset>')
