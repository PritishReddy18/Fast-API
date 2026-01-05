import os

PEPPER = os.environ.get("PEPPER_PASS")

if not PEPPER:
    raise RuntimeError("PEPPER NOT FOUND")