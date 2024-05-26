from helpers.db import MySQLDatabase
from helpers.db2 import *
from helpers.crawlingsele import User


if __name__ == "__main__":
    # Chrome version 125.0.6422.113 (공식 빌드) (64비트)
    user = User()

user.페이지이동(r"https://www.danawa.com/")

# ------------------------------
# 검색창 인지 - AKCSearch
user.객체선택_값입력('//*[@id="AKCSearch"]', "맥북")
user.일반딜레이(1)

# 검색 버튼 클릭
user.객체선택_클릭(
    '//*[contains(concat( " ", @class, " " ), concat( " ", "search__submit", " " ))]'
)
user.일반딜레이(1)

user.객체선택_클릭('//*[@id="opinionDESC"]')  # 상품평많은순
user.일반딜레이(1)

user.객체선택_클릭('//*[@id="productItem12660491"]/div/div[2]/p/a')  # 첫번째 상품 선택
user.일반딜레이(3)

user.새창으로활성이동(1)
user.일반딜레이(3)

# user.객체선택_클릭('//*[@id="bookmark_news_expert_item"]/a/h3')  # 뉴스 커뮤니티
# user.일반딜레이(3)

user.객체선택_클릭(
    '//*[@id="danawa-prodBlog-companyReview-button-tab-companyReview"]'
)  # 상품 리뷰

상품명 = []
리뷰타이틀 = []
리뷰내용 = []

for i in range(10):
    user.일반딜레이(1)
    for j in range(10):
        try:
            상품명.append(
                user.객체선택_텍스트추출(
                    '//*[@id="blog_content"]/div[2]/div[1]/h3/span'
                )
            )
            print(e)
            리뷰타이틀.append(
                user.객체선택_텍스트추출(
                    f'//*[@id="danawa-prodBlog-companyReview-content-wrap-{j}"]/div/div[1]/p'
                )
            )
            print(e)
            리뷰내용.append(
                user.객체선택_텍스트추출(
                    f'//*[@id="danawa-prodBlog-companyReview-content-wrap-{j}"]/div/div[2]'
                )
            )
        except Exception as e:
            print(e)

import pandas as pd

df = pd.DataFrame({"상품명:": 상품명, "리뷰타이틀": 리뷰타이틀, "리뷰내용": 리뷰내용})
df.to_excel(
    r"C:\Users\USER\Documents\GitHub\Web-Crawling\크롤링예제\crawling\runnersele.py",
    index=True,
)
user.일반딜레이(10)
# user.종료()
# user.일반딜레이(3)
