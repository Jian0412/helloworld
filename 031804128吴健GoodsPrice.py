# CrowJDGoodsAndPrice.py
import requests
from bs4 import BeautifulSoup
import lxml

"""
    该程序由于本人技术有限，在爬取页面商品时有个bug一直存在，输出格式也不是非常标准，将就着跑吧。
"""
# 获取链接函数
def GetHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 页面处理函数
def ParsePageAndPrint(html):
    try:
        soup = BeautifulSoup(html, "lxml")
        # 找到商品名称标签
        title = soup.select("div[class='p-name p-name-type-2']")
        # 找到商品价格标签
        price = soup.select("div[class='p-price']")
        tlt = []
        pri = []
        for ti in title:
            # 再找到具体的位置
            em = ti.find("em")
            tlt.append(em.text)
        for pr in price:
            pri.append(pr.text)
        for i in range(len(tlt)):
            # 输出 （字符串函数不精，只能处理到这了）
            print([tlt[i].strip()+" "+pri[i].strip()])
    except:
        print("")


def main():
    start_url = "https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&wq=&pvid=05549535cd974402b9067d405772eeeb"
    url1="https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&qrst=1&wq=%E4%B9%A6%E5%8C%85&stock=1&page=3&s=51&click=0"
    url2="https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&qrst=1&wq=%E4%B9%A6%E5%8C%85&stock=1&page=5&s=101&click=0"
    print("------------这是起始商品页------------")
    html = GetHTMLText(start_url)
    ParsePageAndPrint(html)
    # 这里只是先循环爬取前两个，可以比较前两个url1、url2，只需要对其中一些字符做处理就可以了。
    for i in range(1,3):
        try:
            url="https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&qrst=1&wq=%E4%B9%A6%E5%8C%85&stock=1&page=5&s="+str(51*i)+"&click=0"
            # + str(51 * i)
            print("------------这是第{:2}个商品页------------".format(i))
            htmli = GetHTMLText(url)
            ParsePageAndPrint(htmli)
        except:
            continue


main()