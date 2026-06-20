import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

# ======================
# DATABASE CONFIGURATION
# ======================
#
# Reads DATABASE_URL from the environment (set this in your deployment
# platform's dashboard / .env file). If it's not set, falls back to a
# local SQLite file so the project still runs out of the box for local
# development.
#
# IMPORTANT: SQLite writes to a file on local disk. Most hosting
# platforms (Render, Railway, Heroku, Fly.io, etc.) use ephemeral
# filesystems, so that file -- and all your data -- is wiped on every
# restart/redeploy. Use a managed Postgres database in production to
# avoid this.

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./clinic.db")

# Some platforms (e.g. Heroku) hand out URLs starting with
# "postgres://", but SQLAlchemy 1.4+/2.x requires "postgresql://".
# Normalize it so both forms work.
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://", "postgresql://", 1
    )

# SQLite needs this extra connect arg to work with FastAPI's
# multi-threaded request handling; Postgres does not.
connect_args = (
    {"check_same_thread": False}
    if DATABASE_URL.startswith("sqlite")
    else {}
)

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
