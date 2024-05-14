from flask_jwt_extended import jwt_required
from src.base_crud.http.routes_blueprint import create_crud_blueprint
from src.casos.http.validation import casos_validatable_fields
from src.casos.repositories.sqlalchemy_casos_repository import (
    SQLAlchemyCasossRepository,
)
from src.casos.usecases.manage_casos_usecase import ManageCasosUsecase
from src.frameworks.db.sqlalchemy import SQLAlchemyClient
from src.frameworks.http.flask import create_flask_app
from src.user.http.validation import user_validatable_fields
from src.user.repositories.sqlalchemy_users_repository import SQLAlchemyUsersRepository
from src.user.usecases.manage_users_usecase import ManageUsersUsecase

# Instanciar dependencias.
sqlalchemy_client = SQLAlchemyClient()

# Instanciar repositorios
users_repository = SQLAlchemyUsersRepository(sqlalchemy_client)
casos_repository = SQLAlchemyCasossRepository(sqlalchemy_client)

sqlalchemy_client.create_tables()

# Instanciar casos de uso
manage_users_usecase = ManageUsersUsecase(users_repository)
manage_casos_usecase = ManageCasosUsecase(casos_repository)


casos_blueprint = create_crud_blueprint(
    "casos",
    manage_casos_usecase,
    ["admin","user"],
    creation_validatable_fields=casos_validatable_fields.CASOS_CREATION_VALIDATABLE_FIELDS,
    update_validatable_fields=casos_validatable_fields.CASOS_UPDATE_VALIDATABLE_FIELDS,
)


users_blueprint = create_crud_blueprint(
    "user",
    manage_users_usecase,
    ["admin"],
    creation_validatable_fields=user_validatable_fields.USER_CREATION_VALIDATABLE_FIELDS,
    update_validatable_fields=user_validatable_fields.USER_UPDATE_VALIDATABLE_FIELDS,
)


# Crear blueprints
blueprints = [
    casos_blueprint,
    users_blueprint,
]


# Crear aplicación HTTP con dependencias inyectadas.
app = create_flask_app(blueprints)

for rule in app.url_map.iter_rules():
    # Obtenemos la URL asociada con la regla y los métodos HTTP permitidos
    route_info = {
        "endpoint": rule.endpoint,
        "methods": list(rule.methods - {"HEAD", "OPTIONS"}),  # Ignoramos HEAD y OPTIONS
        "url": str(rule),
    }
    print(route_info)

