# FastAPI Learning Project

> **Note**: This is my first FastAPI project! 🚀 I'm currently learning the basics of FastAPI, so please be kind. 
> If you notice any issues, mistakes, or have suggestions for improvement, I'd love to hear them! 🙏

A simple RESTful API built with FastAPI, SQLAlchemy, and PostgreSQL for learning purposes. This project implements basic user authentication, profile management, and post functionality.

## ⚠️ Disclaimer
This is a learning project and not meant for production use. The code may contain suboptimal practices or security issues as I'm still learning FastAPI and backend development.

-- to download all the packages needed for the project----
run this program in your cmd promt
pip install -r requirements.txt


## 🛠️ Features

- User registration and authentication (JWT tokens)
- User profiles with basic information
- Create, read, update, and delete posts
- Like/unlike posts
- CORS support
- Environment-based configuration
- Database migrations with Alembic

## 🚀 Prerequisites

- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## 🛠️ Installation

1. Clone the repository:

   git clone [your-repo-url]
   cd Fast_API

2. Create and activate a virtual environment:

   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate


3. Install dependencies:

   pip install -r requirements.txt

4. Set up your environment variables:
   - Copy `.env.example` to `.env`
   - Update the database connection string and other variables as needed

5. Set up the database:
   - Create a PostgreSQL database
   - Update the `DATA_BASE` connection string in `.env`
   - Run migrations:
     ```bash
     alembic upgrade head
     ```

## 🚀 Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Documentation

Once the server is running, you can access:

- Interactive API docs: `http://127.0.0.1:8000/docs`
- Alternative API docs: `http://127.0.0.1:8000/redoc`

## 📂 Project Structure

```
Fast_API/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main FastAPI application
│   ├── orm_models/          # SQLAlchemy models
│   ├── api_routers/         # API route handlers
│   ├── security/            # Authentication and security
│   ├── schemas/             # Pydantic models
│   └── validation/          # Data validation
├── alembic/                 # Database migrations
├── .env                     # Environment variables
├── .env.example             # Example environment variables
├── alembic.ini              # Alembic configuration
└── README.md                # This file
```

## 🤝 Contributing

Since this is a learning project, I'm not actively seeking contributions. However, if you'd like to suggest improvements or point out issues, please feel free to open an issue or submit a pull request!

## 📝 Learning Notes

- This project uses FastAPI's dependency injection system
- JWT tokens are used for authentication
- Database operations are handled with SQLAlchemy ORM
- Migrations are managed with Alembic
- Environment variables are loaded using python-dotenv

## 🔒 Security Notes

- Passwords are hashed using bcrypt
- Sensitive configuration is stored in environment variables
- JWT tokens are signed with a private key
- CORS is configured but currently allows all origins (update `origins` in `main.py` for production)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

## 📚 Resources That Helped Me Learn

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Python JWT](https://pyjwt.readthedocs.io/)

---

Built with ❤️ as a learning project. Feel free to explore the code and learn along with me!