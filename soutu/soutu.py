import requests
from lxml import etree
import re
import urllib.request

img = './awesome/plugins/soutu/0.jpg'
url = 'https://saucenao.com/search.php'


async def soutu(img_url):
    try:
        pattern = re.compile(r'url=(.+)]')
        image = pattern.findall(str(img_url))[0]
        save_image(image)
        with open(img, 'rb') as f:
            files = {'file': f}
            r = requests.post(url, files=files)
        tree = etree.HTML(r.text)

        similarity_path = '//div[@class="resultsimilarityinfo"]/text()'
        name_path = '//div[@class="resulttitle"]/strong/text()'
        author_path = '//div[@class="resultcontentcolumn"]/a[@class="linkify"]/text()'
        img_path = '//div[@class="resultimage"]/a[@class="linkify"]/img/@src'

        similarity = tree.xpath(similarity_path)[0]
        if float(similarity[:-1]) < 60:
            return 'could not found image. course of similarity below 60.0%'

        name = tree.xpath(name_path)[0]
        id = tree.xpath(author_path)[0]
        author = tree.xpath(author_path)[1]
        result_img = '[CQ:image,file={}]'.format(tree.xpath(img_path)[0])
        result = """image:{}
        similarity:{}
        name:{}
        id:{}
        author:{}""".format(result_img, similarity, name, id, author)
        # print(result_img)
        return result
    except Exception as e:
        return e


def save_image(imsage):
    urllib.request.urlretrieve(imsage, filename=img)

