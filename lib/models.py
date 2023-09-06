from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Float, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)
engine = create_engine('sqlite:///restuarants.db')
Session = sessionmaker(bind=engine)
session = Session()

# restaurant model
class Restaurant(Base):
    # create restaurant table
    __tablename__ = "restaurants"
    # add restaurant column
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float, nullable=False)
    
     # Define the relationship with Review explicitly
    reviews = relationship("Review", back_populates="restaurant")
    
    # make restaurant object readable
    def __repr__(self):
        return f'<Restaurant name:{self.name}, price:{self.price}>'

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    
    reviews = relationship("Review", back_populates="customer")
    restaurants=relationship("Review",back_populates="customer",overlaps="reviews")
    
 # make customer object readable
    def __repr__(self):
        return f"<Customer {self.first_name} {self.last_name}>"

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Define the relationships explicitly
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")
    