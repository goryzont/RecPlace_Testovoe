from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import JSON, ForeignKey
from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]


class Request(Base):
    __tablename__ = "requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    body_request: Mapped[str]
    answer_request: Mapped[str]
    id_owner_request: Mapped[int] = mapped_column(ForeignKey("users.id"))
