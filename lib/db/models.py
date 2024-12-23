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

    def get_products_as_dict(self):
        """
        Returns a list of dictionaries for all products in the shop.
        """
        products = []
        for product in self.products:
            product_dict = {
                'name': product.name,
                'price': product.price,
                'id': product.id,
                'quantity': product.quantity  # Add quantity directly here
            }
            products.append(product_dict)
        return products


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    shop_id = Column(Integer, ForeignKey('shops.id'))
    shop = relationship("Shop", back_populates="products")
    quantity = Column(Integer, default=1)  # Adding quantity directly to Product

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price}, quantity={self.quantity})>"

    def get_product_as_dict(self):
        """
        Returns a dictionary for the product.
        """
        product_dict = {
            'name': self.name,
            'price': self.price,
            'id': self.id,
            'quantity': self.quantity
        }
        return product_dict


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"
