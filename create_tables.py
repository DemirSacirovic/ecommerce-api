from app.database import engine, Base
from app.models import User, Product, Order

Base.metadata.create_all(bind=engine)
print("Tables created: users, products, orders")

