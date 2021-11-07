import random
import requests
from lxml import html


def get_random_char():
    chars = '1234567890abcdefghijklmnopqrstuvwxyz'
    rand_num = random.randrange(0, len(chars))
    return chars[rand_num]


def get_html():
    url = "https://prnt.sc/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }

    for i in range(6):
        url += get_random_char()

    r = requests.get(url=url, headers=headers)
    return r.text


def get_random_image_url():
    html_page = get_html()
    tree = html.fromstring(html_page)
    try:
        img_url = tree.xpath('//img[@id = "screenshot-image"]/@src')[0]
    except:
        return None
    return img_url
