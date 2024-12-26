import argparse
from db.models import Product, Shop
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

def view_products(shop_name):
    engine = create_engine('your_database_url')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    shop = session.query(Shop).filter_by(name=shop_name).first()
    if shop:
        products = session.query(Product).filter_by(shop_id=shop.id).all()
        for product in products:
            print(f"Product: {product.name}, Price: {product.price}")
    else:
        print(f"No shop found with name: {shop_name}")
    
    session.close()

def main():
    parser = argparse.ArgumentParser(description="Shop Management CLI")
    parser.add_argument('--view-products', type=str, help='View products in a shop')
    
    args = parser.parse_args()

    if args.view_products:
        view_products(args.view_products)

if __name__ == "__main__":
    main()
