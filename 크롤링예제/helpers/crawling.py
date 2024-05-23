from bs4 import BeautifulSoup
import requests
import pandas as pd


# 크롤링 하는 함수
def Crawling():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    cap_info_list = []
    price_list = []
    url_list = []

    for ii in range(9):
        newurl = f"https://www.neweracapkorea.com/shop/shopbrand.html?type=Y&xcode=031&mcode=002&sort=&page={ii+1}"
        response = requests.get(newurl, headers=headers)
        response.status_code
        soup = BeautifulSoup(response.content, "lxml")
        for i in range(20):
            for j in range(5):
                try:
                    cap_info_list.append(
                        soup.select(
                            f"#productClass > div > div.page-body > div.width1200 > div > table > tbody > tr:nth-child({i+2}) > td:nth-child({j+1}) > div > ul > li.dsc"
                        )[0].text
                    )
                    price_list.append(
                        soup.select(
                            f"#productClass > div > div.page-body > div.width1200 > div > table > tbody > tr:nth-child({i+2}) > td:nth-child({j+1}) > div > ul > li.price"
                        )[0].text
                    )
                    url_list.append(
                        soup.select(
                            f"#productClass > div > div.page-body > div.width1200 > div > table > tbody > tr:nth-child({i+2}) > td:nth-child({j+1}) > div > div > a"
                        )[0].attrs["href"]
                    )
                except IndexError as e:
                    continue

    # df = pd.DataFrame(
    #     {"제품명": cap_info_list, "가격": price_list, "상세 페이지 주소": url_list}
    # )
