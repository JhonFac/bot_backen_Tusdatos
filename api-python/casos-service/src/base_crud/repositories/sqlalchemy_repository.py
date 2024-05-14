from contextlib import contextmanager

from flask import jsonify
from sqlalchemy import TIMESTAMP, Column, Integer, String, Table
from src.utils import utils


# Clase base para repositorios con SQLAlchemy
class SQLAlchemyBaseRepository:
    def __init__(self, sqlalchemy_client, entity_class, table_name, columns, test=False):
        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.entity_class = entity_class
        self.table_name = f"{table_name}_test" if test else table_name
        self.test = test
        # Crear tabla de forma imperativa
        self.entity_table = Table(
            self.table_name,
            sqlalchemy_client.mapper_registry.metadata,
            *columns
        )

        sqlalchemy_client.mapper_registry.map_imperatively(entity_class, self.entity_table)

    @contextmanager
    def session_scope(self):
        """Provide a transactional scope around a series of operations."""
        session = self.session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create(self, item):
        print('a guardar')
        print(item)
        with self.session_scope() as session:
            session.add(item)
            session.commit()
        return item

    def get_oder_by_id(self, id_order):
        with self.session_scope() as session:
            item = session.query(self.entity_class).filter_by(id_invoice=id_order, deleted_at=None).all()
        return item

    def get_by_tracking(self, id):
        with self.session_scope() as session:
            item = session.query(self.entity_class).filter_by(tracking_number=id, deleted_at=None).all()
        return item

    def get_by_sku(self, sku):
        with self.session_scope() as session:
            item = session.query(self.entity_class).filter_by(sku=sku, deleted_at=None).first()
        return item

    def get_order_by_id_customer(self, id):
        with self.session_scope() as session:
            item = session.query(self.entity_class).filter_by(id_customer=id, deleted_at=None).all()
        return item
    
    def get_by_name(self, username):
        with self.session_scope() as session:
            item = session.query(self.entity_class).filter_by(username=username, deleted_at=None).first()
        return item
    

    def get_all(self):
        with self.session_scope() as session:
            items = session.query(self.entity_class).filter_by(deleted_at=None).all()
        return items

    def get_by_id(self, id):
        with self.session_scope() as session:
            item = session.query(self.entity_class).filter_by(id=id, deleted_at=None).first()
        return item

    def update(self, id, fields):
        with self.session_scope() as session:
            session.query(self.entity_class).filter_by(id=id, deleted_at=None).update(fields)
            item = session.query(self.entity_class).filter_by(id=id, deleted_at=None).first()
        return item

    def delete(self, id):
        with self.session_scope() as session:
            session.query(self.entity_class).filter_by(id=id).update({"deleted_at": utils.get_current_datetime()})

    def hard_delete(self, id):
        with self.session_scope() as session:
            item = session.query(self.entity_class).get(id)
            session.delete(item)

    def hard_delete_all(self):
        if self.test:
            with self.session_scope() as session:
                session.query(self.entity_class).delete()

    def drop_table(self):
        if self.test:
            self.client.drop_table(self.entity_table)
