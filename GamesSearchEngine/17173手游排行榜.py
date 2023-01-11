import requests
from lxml import etree
import csv

data = []
def spider(offset):
    url = "http://top.17173.com/list-1-0-4-0-0-0-0-0-0-0-"+str(offset)+".html"
    resp = requests.get(url)

    html = etree.HTML(resp.text)

    lis = html.xpath("//*[@class='list-plate js-rank']/li")
    for li in lis:
        title = li.xpath("./div/div[2]/div/a/text()")[0].strip()
        link = li.xpath("./div/div[2]/div/a/@href")[0]
        introduction = li.xpath("./div/div[7]/p/text()")[0].strip().replace("&nbsp;", "").replace("&rdquo;", "").replace("&ldquo;", "")

        list = [title, link, introduction]
        data.append(list)
    write_to_files()

def write_to_files():
    with open("datas.csv", "w", newline='', encoding='utf8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


if __name__=='__main__':
    for i in range(1, 100):
        spider(i)
        print("第"+str(i)+"页已爬取！")






