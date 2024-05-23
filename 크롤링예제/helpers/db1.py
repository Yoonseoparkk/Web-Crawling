from sqlalchemy import engine, create_engine, DateTime, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import sqlalchemy
import pandas as pd

Base = sqlalchemy.orm.declarative_base()


class Newera(Base):
    __tablename__ = "newera"
    id = Column(Integer, primary_key=True)
    productName = Column(String)
    price = Column(Integer)
    url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    Base = sqlalchemy.orm.declarative_base()


class MySQLDatabase:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def add_product(self, productName, price, url):
        session = self.Session()
        product = Newera(productName=productName, price=price, url=url)
        session.add(productName)
        session.commit()
        session.close()

    def get_product_by_username(self, username):
        session = self.Session()
        user = session.query(Newera).filter_by(username=username).first()
        session.close()
        return user

    def get_product_by_price(self, price):
        session = self.Session()
        product = session.query(Newera).filter_by(price=price).first()
        session.close()
        return user

    def update_producte_price(self, productName, new_price):
        session = self.Session()
        product = session.query(Newera).filter_by(productName=productName).first()
        if product:
            product.price = new_price
            session.commit()
        session.close()

    def delete_product(self, productName):
        session = self.Session()
        product = session.query(Newera).filter_by(productName=productName).first()
        if product:
            session.delete(product)
            session.commit()
        session.close()

    # def to_sql(self, df):
    #     df = pd.read_excel(
    #         r"C:\Users\USER\Documents\GitHub\Web-Crawling\크롤링예제\뉴에라.xlsx"
    #     )
    #     try:
    #         df.to_sql(name="newera", con=self.engine)
    #         print("로그 남기기")
    #     except Exception as e:
    #         print(e)
    def to_sql(self):
        df = pd.read_excel(
            r"C:\Users\USER\Documents\GitHub\Web-Crawling\크롤링예제\뉴에라.xlsx"
        )
        try:
            df.to_sql(name="newera", con=self.engine)
            print("로그 남기기")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        user = "root"
        password = ""
        host = "localhost"
        port = 3306
        db = "test"

        db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        db = MySQLDatabase(db_url)

    except Exception as e:
        print("DB부분처리안됨")
        print("e")
