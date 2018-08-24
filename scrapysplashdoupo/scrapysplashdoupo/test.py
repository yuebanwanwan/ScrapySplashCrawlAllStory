import scrapy
import requests
from lxml import etree

base_urls = 'http://www.biquge.com.tw/1_1999/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
response = requests.get(base_urls,headers = headers)
html = etree.HTML(response.text)
relatedstory = []
base = 'http://www.biquge.com.tw'
if response.status_code == 200:
    print('111')
    ips = []
    charptersip = html.xpath('//div[@id="list"]//dd/a/@href')
    print(type(charptersip))
    if charptersip:
        for charptes in charptersip:
            #print(charptes)
            ips.append(base + charptes)
    relatedstory = html.xpath('//div[@class="footer_link"]//a/@href')
for i in range(0,len(relatedstory)-1):
    relatedstory[i] = base + relatedstory[i]

print(relatedstory)
print(ips)
