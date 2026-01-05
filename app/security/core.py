from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated = "auto",
    argon2__type = "ID",
    argon2__time_cost = 4,
    argon2__memory_cost = 131072,
    argon2__parallelism = 2,
)