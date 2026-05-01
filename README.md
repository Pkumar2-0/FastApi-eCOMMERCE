# 🛒 FastAPI eCommerce Backend

A lightweight eCommerce backend built using FastAPI and SQLite.
This project demonstrates REST API development, database integration, and clean backend architecture.

---

## 🚀 Tech Stack

* Python 3.x
* FastAPI
* SQLite
* SQLAlchemy
* Uvicorn

---

## 📁 Project Structure

```
ecommerce/
│
├── app/
│   ├── main.py          # Entry point
│   ├── database.py      # DB connection
│   ├── models.py        # Tables
│   ├── schemas.py       # Pydantic models
│   └── routes.py        # API routes
│
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/ecommerce-fastapi.git
cd ecommerce-fastapi
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate it:

* Windows:

```
venv\Scripts\activate
```

* Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Server

```
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI provides automatic interactive docs:

* Swagger UI:
  http://127.0.0.1:8000/docs

* ReDoc:
  http://127.0.0.1:8000/redoc

---

## 📦 Features

* ✅ Create Product
* ✅ Get All Products
* 🔜 User Authentication (JWT)
* 🔜 Cart System
* 🔜 Order Management

---

## 🧪 Example API Usage

### Create Product

**POST** `/products/`

```
{
  "name": "iPhone",
  "price": 999,
  "description": "Apple smartphone"
}
```

---

### Get Products

**GET** `/products/`

---

## 🗄️ Database

* SQLite database file: `ecommerce.db`
* Automatically created on first run

---

## ⚠️ Limitations

* SQLite is suitable for development and small-scale apps
* Not recommended for high concurrency production systems

---

## 🚀 Future Improvements

* JWT Authentication
* Payment Integration
* Admin Dashboard
* Product Categories & Filters
* Deployment (Docker / Cloud)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.
