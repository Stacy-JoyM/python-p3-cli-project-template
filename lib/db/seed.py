from faker import Faker
from .database import setup_database
from .models import Shop, Product, Item, User

def seed_data():
    session = setup_database()
    faker = Faker()

    # Create Shops
    for _ in range(3):
        shop = Shop(name=faker.company(), location=faker.city())
        session.add(shop)

        # Add Products to Shop
        for _ in range(5):
            product = Product(
                name=faker.word(),
                price=faker.random_int(min=10, max=100),
                shop=shop
            )
            session.add(product)

            # Add Items for Product
            for _ in range(3):
                item = Item(product=product, quantity=faker.random_int(min=1, max=20))
                session.add(item)

    # Create Users
    for _ in range(5):
        user = User(name=faker.name(), email=faker.email())
        session.add(user)

    session.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
