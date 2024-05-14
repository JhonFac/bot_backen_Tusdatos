from flask import jsonify
from flask_jwt_extended import create_access_token
from src.utils import utils


class BaseManageUsecase:
    def __init__(self, repository, _object, _object_name):
        self.repository = repository
        self._object= _object
        self._object_name= _object_name
        print(self._object_name)

    def get_token(self, data):
        print(data)
        username = data.get("username")
        password = data.get("password")
        item = self.get_by_name(username)
        if item is None:
            raise ValueError(f"User {username} doesn't exist.")

        user = item.serialize()
        print(user)
        if user['password_hash'] == password:
            return create_access_token(identity=user['role'])
        return False
    
    def get_by_name(self, name):
        return self.repository.get_by_name(name)


    def get_oder_by_id(self, item_id):
        item = self.repository.get_oder_by_id(item_id)
        if item is None:
            raise ValueError(f"Item with ID {item_id} doesn't exist.")
        return item

    def get_all(self):
        # Retorna una lista de entidades desde el repositorio.
        return self.repository.get_all()

    def get_by_id(self, item_id):
        item = self.repository.get_by_id(item_id)
        if item is None:
            raise ValueError(f"Item with ID {item_id} doesn't exist.")
        return item

    def create(self, data):
        print('entro a crear')
        # Crea una instancia desde la data recibida, que ya debe venir validada desde afuera,
        # y guarda dicha instancia en el repositorio para finalmente retornarla.
            
        current_time = utils.get_current_datetime()
        data["created_at"] = current_time
        data["updated_at"] = current_time
        item = self._object.from_dict(data)
        item = self.repository.create(item)
        print(f'esto es lo que retorno: {item}')

        return item

    def update(self, item_id, data):

        # Actualiza los datos recibidos y los guarda en el repositorio según la ID recibida.
        # La data no necesariamente debe contener todos los campos de la entidad, sólo
        # los campos que se van a actualizar. Esta data debe venir validada desde afuera.

        item = self.get_by_id(item_id)
        if item:
            data["updated_at"] = utils.get_current_datetime()
            item = self.repository.update(item_id, data)
            return item
        else:
            raise ValueError(f"{self._object_name} of ID {item_id} doesn't exist.")
   
    def delete(self, item_id):

        # Realiza un soft-delete del libro con la ID especificada, si es que existe.
        # A nivel de repositorio realiza una actualización al campo "deleted_at".

        item = self.get_by_id(item_id)

        if item:
            data = {"deleted_at": utils.get_current_datetime()}
            self.repository.update(item_id, data)
        else:
            raise ValueError(f"{self._object_name} of ID {item_id} doesn't exist or is already deleted.")