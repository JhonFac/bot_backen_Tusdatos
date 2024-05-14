from enviame.inputvalidation import FAIL_CODE, SUCCESS_CODE, validate_schema_flask
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from src.utils.rol_autentication import role_required


# Crea un blueprint CRUD para una entidad genérica
def create_crud_blueprint(resource_name, use_case, roles, # The `creation_validatable_fields`
# parameter in the `create_crud_blueprint`
# function is used to specify the fields
# that need to be validated when creating a
# new entity of the specified resource. This
# parameter is used in conjunction with the
# `validate_schema_flask` decorator to
# ensure that the incoming request data
# adheres to a specific schema before
# processing the creation operation. By
# providing the
# `creation_validatable_fields`, you can
# enforce validation rules on the request
# body before creating a new entity, helping
# to maintain data integrity and consistency
# in the application.
# The `creation_validatable_fields`
# parameter in the `create_crud_blueprint`
# function is used to specify the fields
# that need to be validated when creating a
# new entity of the specified resource. This
# parameter is used in conjunction with the
# `validate_schema_flask` decorator to
# ensure that the incoming request data
# adheres to a specific schema before
# processing the creation operation. By
# providing the
# `creation_validatable_fields`, you can
# enforce validation rules on the request
# body before creating a new entity, helping
# to maintain data integrity and consistency
# in the application.
creation_validatable_fields=None, update_validatable_fields=None):

    blueprint = Blueprint(resource_name, __name__)

    print(roles)



    if resource_name == 'user':
        @blueprint.route(f"/{resource_name}/login", methods=["POST"])
        def login():
            try:
                body = request.get_json()
                token = use_case.get_token(body)
                if token:
                    response = {
                        "code": SUCCESS_CODE,
                        "message": "Token obtained successfully.",
                        "data":token,
                    }
                    return response, 200
                else:
                    response = {
                        "code": FAIL_CODE,
                        "message": "Token creation failed",
                    }
                    return response, 404

            except ValueError as e:
                response = {
                    "code": FAIL_CODE,
                    "message": str(e),
                }
                return response, 400




    @blueprint.route(f"/{resource_name}", methods=["GET"])
    @jwt_required()
    @role_required(*roles)
    def get_all():
        items = use_case.get_all()
        items_dict = [item.serialize() for item in items]
        response = {
            "code": SUCCESS_CODE,
            "message": f"{resource_name.capitalize()}s obtained successfully.",
            "data": items_dict,
        }
        return response, 200

    @blueprint.route(f"/{resource_name}/<string:item_id>", methods=["GET"])
    @jwt_required()
    @role_required(*roles)
    def get_by_id(item_id):
        try:
            item = use_case.get_by_id(item_id)
            response = {
                "code": SUCCESS_CODE,
                "message": f"{resource_name.capitalize()} obtained successfully.",
                "data": item.serialize(),
            }
            return response, 200
        except ValueError as e:
            response = {
                "code": FAIL_CODE,
                "message": str(e),
            }
            return response, 400

    @blueprint.route(f"/{resource_name}", methods=["POST"])
    @jwt_required()
    @role_required(*roles)
    @validate_schema_flask(creation_validatable_fields)
    def create():
        body = request.get_json()
        print(body)
        try:
            item = use_case.create(body)
            response = {
                "code": SUCCESS_CODE,
                "message": f"{resource_name.capitalize()} created successfully.",
                "data": item.serialize(),
            }
            return response, 201
        except ValueError as e:
            response = {
                "code": FAIL_CODE,
                "message": str(e),
            }
            return response, 400

    @blueprint.route(f"/{resource_name}/<string:item_id>", methods=["PUT"])
    @jwt_required()
    @role_required(*roles)
    @validate_schema_flask(update_validatable_fields)
    def update(item_id):
        body = request.get_json()
        try:
            item = use_case.update(item_id, body)
            response = {
                "code": SUCCESS_CODE,
                "message": f"{resource_name.capitalize()} updated successfully.",
                "data": item.serialize(),
            }
            return response, 200
        except ValueError as e:
            response = {
                "code": FAIL_CODE,
                "message": str(e),
            }
            return response, 400

    @blueprint.route(f"/{resource_name}/<string:item_id>", methods=["DELETE"])
    @jwt_required()
    @role_required(*roles)
    def delete(item_id):
        try:
            use_case.delete(item_id)
            response = {
                "code": SUCCESS_CODE,
                "message": f"{resource_name.capitalize()} with ID {item_id} deleted successfully.",
            }
            return response, 200
        except ValueError as e:
            response = {
                "code": FAIL_CODE,
                "message": str(e),
            }
            return response, 400

    return blueprint
