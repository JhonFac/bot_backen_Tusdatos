from src.utils.utils import format_date

# Entidad representando a un libro.

class Casos():

    def __init__(self, id, no_causa , fecha, hora, tipificacion, contenido, created_at = None, updated_at = None, deleted_at = None):

        self.id = id
        self.no_causa = no_causa
        self.fecha = fecha
        self.hora = hora
        self.tipificacion = tipificacion
        self.contenido = contenido

        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at

    def to_dict(self):

        # Transforma los campos de este objeto a un diccionario,
        # útil para guardar contenido en los repositorios.

        return {
            "id": self.id,
            "no_causa": self.no_causa,
            "fecha": self.fecha,
            "hora": self.hora,
            "tipificacion": self.tipificacion,
            "contenido": self.contenido,
            
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
        }

    def serialize(self):

        # Retorna un diccionario serializable a JSON.
        # Es parecido a "to_dict", pero es útil para mostrar datos en el exterior,
        # como por ejemplo retornar una respuesta hacia al usuario desde el endpoint.
        # En este caso no se retorna la fecha "deleted_at", ya que es información
        # privada, y las fechas se transforman a un formato legible.

        data = self.to_dict()
        
        data.pop("deleted_at")
        
        data["created_at"] = format_date(data["created_at"])
        data["updated_at"] = format_date(data["updated_at"])

        return data

    @classmethod
    def from_dict(cls, dict):

        # Retorna una instancia de este objeto desde un diccionario de datos,
        # para no tener que llamar al constructor pasando los datos uno a uno.
        # Si un campo falta en el diccionario, se asume valor None.

        id = dict.get("id")
        no_causa = dict.get("no_causa")
        fecha = dict.get("fecha")
        hora = dict.get("hora")
        tipificacion = dict.get("tipificacion")
        contenido = dict.get("contenido")

        created_at = dict.get("created_at")
        updated_at = dict.get("updated_at")
        deleted_at = dict.get("deleted_at")

        return Casos(id, no_causa, fecha, hora, tipificacion, contenido, created_at, updated_at, deleted_at)