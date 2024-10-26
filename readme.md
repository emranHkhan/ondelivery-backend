# Restaurant Management System API Documentation

## Table of Contents
- [Overview](#overview)
- [Base URL](#base-url)
- [Authentication](#authentication)
- [API Endpoints](#api-endpoints)
  - [User API](#user-api)
  - [Food Item API](#food-item-api)
  - [Order API](#order-api)
  - [Restaurant API](#restaurant-api)
  - [Category API](#category-api)
  - [Review API](#review-api)

## Overview
This API provides endpoints for managing a restaurant system, including users, food items, orders, restaurants, categories, and reviews.

## Base URL
```
http://your-domain.com/api/
```

## Authentication
The API uses Django's built-in authentication system. Most endpoints require authentication via:
- Token Authentication
- Session Authentication

To authenticate requests, include the token in the header:
```
Authorization: Token <your-token>
```

## API Endpoints

### User API
Base path: `/api/users/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register/` | POST | Register a new user |
| `/login/` | POST | User login |
| `/profile/` | GET | Get user profile |
| `/profile/` | PUT | Update user profile |

### Food Item API
Base path: `/api/food-items/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List all food items |
| `/` | POST | Create new food item |
| `/<id>/` | GET | Get food item details |
| `/<id>/` | PUT | Update food item |
| `/<id>/` | DELETE | Delete food item |

### Order API
Base path: `/api/orders/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List user orders |
| `/` | POST | Create new order |
| `/<id>/` | GET | Get order details |
| `/<id>/status/` | PUT | Update order status |
| `/history/` | GET | Get order history |

### Restaurant API
Base path: `/api/restaurants/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List all restaurants |
| `/` | POST | Register new restaurant |
| `/<id>/` | GET | Get restaurant details |
| `/<id>/` | PUT | Update restaurant info |
| `/<id>/menu/` | GET | Get restaurant menu |

### Category API
Base path: `/api/categories/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List all categories |
| `/` | POST | Create new category |
| `/<id>/` | GET | Get category details |
| `/<id>/` | PUT | Update category |
| `/<id>/items/` | GET | Get items in category |

### Review API
Base path: `/api/reviews/`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | List all reviews |
| `/` | POST | Create new review |
| `/<id>/` | GET | Get review details |
| `/<id>/` | PUT | Update review |
| `/<id>/` | DELETE | Delete review |

## Request/Response Examples

### Register User
```http
POST /api/users/register/
Content-Type: application/json

{
    "username": "user123",
    "email": "user@example.com",
    "password": "securepassword"
}
```

### Create Order
```http
POST /api/orders/
Content-Type: application/json
Authorization: Token <your-token>

{
    "restaurant_id": 1,
    "items": [
        {
            "item_id": 1,
            "quantity": 2
        },
        {
            "item_id": 3,
            "quantity": 1
        }
    ],
    "delivery_address": "123 Main St"
}
```

## Error Handling

The API uses standard HTTP response codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error




