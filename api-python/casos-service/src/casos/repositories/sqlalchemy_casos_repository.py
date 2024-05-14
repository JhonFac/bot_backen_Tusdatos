from sqlalchemy import TIMESTAMP, Column, Integer, String, Text
from src.base_crud.repositories.sqlalchemy_repository import SQLAlchemyBaseRepository
from src.casos.entities.casos import Casos


# Repositorio para la entidad Casos
class SQLAlchemyCasossRepository(SQLAlchemyBaseRepository):
    def __init__(self, sqlalchemy_client, test=False):
        columns = [
            Column("id", Integer, primary_key=True),
            Column("no_causa", String(100)),
            Column("fecha", String(100)),
            Column("hora", String(100)),
            Column("tipificacion", String(100)),
            Column("contenido", Text),
            Column("created_at", TIMESTAMP),
            Column("updated_at", TIMESTAMP),
            Column("deleted_at", TIMESTAMP, nullable=True),
        ]
        super().__init__(sqlalchemy_client, Casos, "Casoss", columns, test)
