from src.utils.utils import format_date


# Clase base para entidades con campos comunes
class BaseEntity:
    def __init__(self, id, **kwargs):
        self.id = id
        self.created_at = kwargs.get("created_at")
        self.updated_at = kwargs.get("updated_at")
        self.deleted_at = kwargs.get("deleted_at")

    def to_dict(self):
        # Convierte la entidad a un diccionario, útil para guardar contenido en repositorios
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
        }

    def serialize(self):
        # Retorna un diccionario serializable a JSON, útil para responder a peticiones HTTP
        data = self.to_dict()
        # Remover información sensible
        data.pop("deleted_at", None)
        # Formatear fechas para que sean legibles
        data["created_at"] = format_date(data["created_at"])
        data["updated_at"] = format_date(data["updated_at"])
        return data

    @classmethod
    def from_dict(cls, data):
        # Crea una instancia de la entidad desde un diccionario de datos
        id = data.get("id")
        # Usamos "kwargs" para mantener la flexibilidad para entidades hijas
        return cls(id, **data)
