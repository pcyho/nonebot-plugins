import requests
from lxml import etree
import re


async def get_fomo_info():
    # 电商链接平台
    url = "https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&fr=auc_top&p=%E3%81%B5%E3%82%82%E3%81%B5%E3%82%82&x=0&y=0"
    # 路径
    xpath = '/html/body/script[5]/text()'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # 获取信息
    try:
        r = requests.get(url, headers=headers)
    except Exception as e:
        return e

    r.encoding = r.apparent_encoding
    # print(r.text)
    html = etree.HTML(r.text)
    # 解析html
    items = html.xpath(xpath)
    list = items[0].split(";")[0]

    pattern1 = re.compile(r'"productName" : "(.+)",')
    pattern2 = re.compile(r'"price" : "(\d+)"')
    pattern3 = re.compile(r'"productID" : "(\w?\d+)"')
    id = pattern3.findall(list)

    name = pattern1.findall(list)

    price = pattern2.findall(list)
    # 返回信息
    info = ''
    for i in range(len(id)):
        info = info + "ID:" + id[i] + '\nname:' + name[i] + "\nprice:" + price[i] + "\n"
    return info
