# main.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Category, Product

# Connect to SQLite database (creates db.sqlite3 if it doesn't exist)
engine = create_engine('sqlite:///db.sqlite3', echo=True)

# Create tables
Base.metadata.create_all(engine)

# Start a session
Session = sessionmaker(bind=engine)
session = Session()

# Clear existing data (optional)
session.query(Product).delete()
session.query(Category).delete()
session.commit()

# Add sample categories
categories = [
    Category(category_name='Electronics'),
    Category(category_name='Books'),
    Category(category_name='Clothing')
]
session.add_all(categories)
session.commit()

# Add sample products
products = [
    Product(product_name='Laptop', price=899.99, category_id=categories[0].category_id),
    Product(product_name='Smartphone', price=699.99, category_id=categories[0].category_id),
    Product(product_name='Python Programming Book', price=29.99, category_id=categories[1].category_id),
    Product(product_name='T-Shirt', price=15.00, category_id=categories[2].category_id)
]
session.add_all(products)
session.commit()

# Retrieve and print product details
print("\nProduct List:")
products = session.query(Product).all()
for product in products:
    print(f"Product: {product.product_name}, Price: ${product.price}, Category: {product.category.category_name}")
