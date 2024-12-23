from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    products = relationship("Product", back_populates="shop")

    def __repr__(self):
        return f"<Shop(name='{self.name}', location='{self.location}')>"

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    shop_id = Column(Integer, ForeignKey('shops.id'))
    shop = relationship("Shop", back_populates="products")
    items = relationship("Item", back_populates="product")

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price})>"

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer, default=1)
    product = relationship("Product", back_populates="items")

    def __repr__(self):
        return f"<Item(product_id={self.product_id}, quantity={self.quantity})>"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"
