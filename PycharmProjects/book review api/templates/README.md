# 📚 Book Review API

This is a RESTFUl API for managing books and user-submitted reviews, built using Django REST Framework.

## 🚀 Features

- User registration
- JWT authentication
- Change password
- Admin can add, update, delete books
- Users can browse and review books
- Each user can edit/delete only their reviews
- Swagger and Redoc documentation

---

## 🛠 Technologies Used

- Python 3
- Django 4+
- Django REST Framework
- djangorestframework-simplejwt
- SQLite (default DB)
- drf-yasg (Swagger UI)

---

## 📁 Project Structure

book-review-api/ ├── book_review_api/ # Project settings ├── reviews/ # App: reviews & books ├── db.sqlite3 # Database ├── manage.py └── README.md


---


---

## ⚙️ Setup Instructions

```bash
1. Clone the repository:
git clone https://github.com/fadiyah2/book-review-api.git
cd book-review-api

2. Create and activate a virtual environment:
python -m venv .venv
.venv\Scripts\activate  # on Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run migrations:
python manage.py makemigrations
python manage.py migrate

5. Create superuser:
python manage.py createsuperuser

6. Run the server:
python manage.py runserver
```

## 🔐 Authentication

This API uses **JWT Authentication** with `djangorestframework-simplejwt`.

### 🔑 Endpoints:

- `POST /api/register/` — Register a new user  
- `POST /api/token/` — Obtain JWT tokens (access and refresh)  
- `POST /api/token/refresh/` — Refresh your access token  
- `POST /api/change-password/` — Change the logged-in user's password  

---

## 📚 Book Endpoints

| Method | Endpoint             | Description                      |
|--------|----------------------|----------------------------------|
| GET    | /api/books/          | List all books                   |
| GET    | /api/books/{id}/     | Retrieve book details            |
| POST   | /api/books/          | Add book (Admin only)            |
| PUT    | /api/books/{id}/     | Edit book (Admin only)           |
| DELETE | /api/books/{id}/     | Delete book (Admin only)         |

---

## ✍️ Review Endpoints

| Method | Endpoint                              | Description                    |
|--------|---------------------------------------|--------------------------------|
| POST   | /api/books/{book_id}/reviews/         | Add a review to a book         |
| GET    | /api/books/{book_id}/reviews/         | Get all reviews for a book     |
| PUT    | /api/reviews/{id}/                    | Edit a review (owner only)     |
| DELETE | /api/reviews/{id}/                    | Delete a review (owner only)   |

---
## Testing the API with Postman
1. Register a new user:
POST /api/register/
Body (JSON):
{
  "username": "fadia",
  "password": "123456",
  "email": "fadia@example.com"
}

2. Get your JWT token:
POST /api/token/
Body (JSON):
{
  "username": "fadia",
  "password": "123456"
}

3. Add this header for protected endpoints:
Authorization: Bearer your_token_here

4. Change password:
POST /api/change-password/
Body (JSON):
{
  "old_password": "123456",
  "new_password": "newpass123"
}

## 📄 API Documentation

- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

You can test all endpoints directly from the Swagger interface.

---

## ✅ Final Notes

- ✅ Only **admins** can create, update, or delete books.  
- ✅ All **authenticated users** can add reviews.  
- ✅ Users can only **edit/delete their own reviews**.  
- ✅ All endpoints are protected with proper **authentication and permissions**.  
- ✅ Make sure to apply **migrations** and create a **superuser** before testing.  
- ✅ Hosted locally at: [http://127.0.0.1:8000](http://127.0.0.1:8000)











