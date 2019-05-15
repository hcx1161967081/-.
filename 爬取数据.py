周强 2019/5/15 15:12:26
import requests
from bs4 import BeautifulSoup
import urllib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

def get_good_urls(word):
    url_str = urllib.parse.quote(word)
    urls = (
    "https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=4&page={}&s=1&click=0".format(
        url_str, i) for i in range(1, 12, 2))
    return urls


def get_html(url):
    html = requests.get(url, headers=headers)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text, 'lxml')
    return soup


def get_info(soup):
    all_titles = soup.find_all(class_="p-name p-name-type-2")
    all_prices = soup.find_all(class_="p-price")
    all_commits = soup.find_all(class_="p-commit")


    titles = []
    prices = []
    commits = []

    for title in all_titles:
        titles.append(title.text.strip())

    for price in all_prices:
        prices.append(price.text.strip())

    for commit in all_commits:
        commits.append(commit.text.strip())
    write_data(prices, len(prices))
    return titles, prices, commits
def write_data(list, num):
    # with open('E:/Crawler/case/taob2.txt', 'a') as data:
    #    print(list, file=data)
    print("文本写入中")
    for i in range(num):# num控制把爬取到的商品写进多少到文本中

        u = list[i]
        with open('d:/taobao.txt', 'a') as data:
            print(u, file=data)


if __name__ == '__main__':
    good = input("请输入你要查询的商品\n")
    links = get_good_urls(good)
    for link in links:
        html = get_html(link)
        ti, pr, co= get_info(html)
