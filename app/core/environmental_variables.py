from dotenv import load_dotenv
import os

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY")
TOKEN_EXPIRE_IN_MINUTES = os.environ.get("TOKEN_EXPIRE_IN_MINUTES",30)
ALGORITHM = os.environ.get("ALGORITHM")