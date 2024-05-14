from sqlalchemy import TIMESTAMP, Column, Integer, String
from src.base_crud.repositories.sqlalchemy_repository import SQLAlchemyBaseRepository
from src.user.entities.user import User


# Repositorio para la entidad User
class SQLAlchemyUsersRepository(SQLAlchemyBaseRepository):
    def __init__(self, sqlalchemy_client, test=False):
        columns = [
            Column("id", Integer, primary_key=True),
            Column("username", String(50)),
            Column("password_hash", String(250)),
            Column("role", String(100)),
            Column("status", String(100)),
            Column("created_at", TIMESTAMP),
            Column("updated_at", TIMESTAMP),
            Column("deleted_at", TIMESTAMP, nullable=True),
        ]
        super().__init__(sqlalchemy_client, User, "UsersD", columns, test)




        