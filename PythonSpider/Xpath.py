import requests
from lxml import etree
url = "https://guangdong.zbj.com/rjkf/f.html?r=1"
head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70"
}
resq = requests.get(url=url, headers=head).text
tree = etree.HTML(resq)
divs = tree.xpath("//div[@class='search-result-list-service']/div")
prices = tree.xpath(".//div[@class='price']/span/text()")
# print(prices)
for div in divs:
    price = div.xpath(".//div[@class='price']/span/text()")[0].strip("￥").strip("狂欢价").strip("：¥") + '元'
    comname = div.xpath(".//div[@class='bot-content']/a/text()")[0]
    print(price)
    print(comname)