from src.base_crud.usecases.manage_usecase import BaseManageUsecase
from src.user.entities.user import User


# Recibe en el constructor el repositorio a utilizar. Da igual si recibe el repositorio
# de SQL o de FireUser, el caso de uso debe funcionar independientemente de su implementación.
class ManageUsersUsecase(BaseManageUsecase):
    def __init__(self, repository):
        super().__init__(repository, User, "User")

