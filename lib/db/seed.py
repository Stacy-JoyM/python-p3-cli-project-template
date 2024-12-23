from database import setup_database
from models import Shop, Product, User  # Import all your models

def query_all_shops():
    session = setup_database()  # Setup the database session
    shops = session.query(Shop).all()  # Query all shops
    if shops:
        print("All Shops:")
        for shop in shops:
            print(f"Shop Name: {shop.name}, Location: {shop.location}")
    else:
        print("No shops found in the database.")
    session.close()

def query_all_products():
    session = setup_database()  # Setup the database session
    products = session.query(Product).all()  # Query all products
    if products:
        print("\nAll Products:")
        for product in products:
            print(f"Product Name: {product.name}, Price: {product.price}, Shop ID: {product.shop_id}")
    else:
        print("No products found in the database.")
    session.close()

def query_all_users():
    session = setup_database()  # Setup the database session
    users = session.query(User).all()  # Query all users
    if users:
        print("\nAll Users:")
        for user in users:
            print(f"User Name: {user.name}, Email: {user.email}")
    else:
        print("No users found in the database.")
    session.close()

def query_all_tables():
    # Query all tables in the database
    query_all_shops()
    query_all_products()
    query_all_users()

if __name__ == "__main__":
    # Query and display all tables' data
    query_all_tables()
