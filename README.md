# code-challenge-restaurants

## Intoduction
This Python application manages restaurant reviews, customers, and reviews for restaurants by implementing SQLAlchemy for data storage and relationships between models.

## Table of Contents
- Setup
- Usage
- Features
- Models
- Methods
- License

## Setup 
1. Clone the repository to your local machine
```bash
git clone https://github.com/yourusername/restaurant-reviews.git
```
2. Navigate to the project directory
```bash
cd restaurant-reviews
```
3. Install the required packages using pip

## Usage 
1. Run the application using python
```bash
python3 app.py
```
2. Access the application through your web browser or API client
3. Use the various features to manage restaurant reviews and customers

## Features 
. View restaurant reviews
. Add new reviews
. Find The customer's favorite restaurant
. Get the fanciest restaurant
. Delete all reviews for a restaurant
. Retrieve all reviews for a restaurant

## Models
- 'Restaurant': Represents a restaurant with a name and price.
- 'Customer': Represents a customer with a first name and a last name.
- 'Review': Represents a review with a star rating, associated with both a restaurant and a customer.

## Methods
### Review

- 'customer()': Returns the Customer instance associated with this review.
- 'restaurant()': Returns the Restaurant instance associated with this review.
- 'full_review()': Returns a formatted string with the review details.

## Restaurant
- 'reviews()': Returns a collection of all reviews for the restaurant.
- 'customers()': Returns a collection of all customers who reviewed the restaurant.
- 'fanciest()': Returns the restaurant instance with the highest price.
- 'all_reviews()': Returns a list of formatted strings for all reviews of the restaurant.

## Customer
- 'reviews()': Returns a collection of all reviews left by the customer.
- 'restaurants()': Returns a collection of all restaurants reviewed by the customer.
- 'full_name()': Returns the full name of the customer (first name and last name).
- 'favorite_restaurant()': Returns the restaurant instance with the highest star rating from this customer.
- 'add_review(restaurant, rating)': Adds a new review for the specified restaurant and rating.
- 'delete_reviews(restaurant)': Deletes all reviews for the specified restaurant.

## License 
This project is licensed under the MIT License

