# Constantes que definen el "esquema" del payload que hay que validar
# para el caso de crear o actualizar un libro. Estos esquemas son usados
# en el decorador "validate_schema_flask" usado en los blueprints.

# La diferencia entre el esquema de creación y el de actualización es que
# en este último los campos son opcionales, y en algunos casos algunos campos
# podrían sólo definirse en la creación pero no permitir su actualización.

CASOS_CREATION_VALIDATABLE_FIELDS = {

    "no_causa": {
        "required": True,
        "type": "string",
    },

    "fecha": {
        "required": True,
        "type": "string",
    },

    "hora": {
        "required": True,
        "type": "string",
    },

    "tipificacion": {
        "required": True,
        "type": "string",
    },

    "contenido": {
        "required": True,
        "type": "string",
    },
}


CASOS_UPDATE_VALIDATABLE_FIELDS = {

    "no_causa": {
        "required": False,
        "type": "string",
    },

    "fecha": {
        "required": False,
        "type": "string",
    },

    "hora": {
        "required": False,
        "type": "string",
    },

    "tipificacion": {
        "required": False,
        "type": "string",
    },

    "contenido": {
        "required": False,
        "type": "string",
    },
}
