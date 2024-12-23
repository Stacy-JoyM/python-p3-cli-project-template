from db.database import setup_database
from db.models import Shop, Product

def view_shops(session):
    shops = session.query(Shop).all()
    for shop in shops:
        print(shop)

def view_products(session):
    products = session.query(Product).all()
    for product in products:
        print(product)

def main():
    session = setup_database()
    print("Welcome to the Shop Management CLI!")
    
    while True:
        print("\nOptions:")
        print("1. View Shops")
        print("2. View Products")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_shops(session)
        elif choice == "2":
            view_products(session)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
