from datetime import datetime

import sqlalchemy
from sqlalchemy import MetaData, Table, Column, TIMESTAMP, INTEGER, String, ForeignKey, JSON

metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", INTEGER, primary_key=True),
    Column("name", String(255), unique=True, nullable=False),
    Column("permission", JSON)

)

users = Table(
    "users",
    metadata,
    Column("id", INTEGER, primary_key=True),
    Column("email", String(255), unique=True, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registred_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", INTEGER, ForeignKey("roles.id"))
)

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)